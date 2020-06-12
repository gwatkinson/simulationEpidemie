""" Classe Personne pour créer les individus de la simulation """


import numpy as np
import random as rd
import matplotlib.pyplot as plt


class Personne:

    def __init__ (self,**kwargs):
        self.x=kwargs.get("x",0) #abscisse de l'individu
        self.y=kwargs.get("y",0) #ordonnée de l'individu
        self.statut=kwargs.get("statut","sain") # statut : sain,malade (3 échelles),mort,rétabli
        self.temps_infection=kwargs.get("temps_infection",0) # durée de la maladie
        self.sensx=kwargs.get("u_x", 2*rd.random()-1) # sens horizontal de déplacement
        self.sensy=kwargs.get("u_y", 2*rd.random()-1) # sens vertical de déplacement
        self.respect=kwargs.get("respect","oui") # respect ou non des mesures de confinement


# Le déplacement se fait dans le même sens tant que l'individu n'est pas au niveau des bords
    def deplacement_normal (self,amplitude):
        dl=rd.random()*amplitude
        dx=dl*self.sensx
        dy=dl*self.sensy
        while self.x+dx>100 or self.x+dx<0 or self.y+dy>100 or self.y+dy<0:
            self.sensx=2*rd.random()-1
            p=rd.random()
            if p<0.5:
                self.sensy=(1-self.sensx**2)**0.5
            else:
                self.sensy=-(1-self.sensx**2)**0.5
            dl=rd.random()*amplitude
            dx=dl*self.sensx
            dy=dl*self.sensy
        self.x=self.x +dx
        self.y=self.y +dy


# Dans le cas de l'isolement, le déplacement devient aléatoire et d'amplitude 10 fois plus petite.
    def deplacement_isolement (self,amplitude):
            dx,dy=(2*rd.random()-1)*(amplitude/10), (2*rd.random()-1)*(amplitude/10)
            while self.x+dx>100 or self.x+dx<0 or self.y+dy>100 or self.y+dy<0:
                dx,dy=(2*rd.random()-1)*(amplitude/10), (2*rd.random()-1)*(amplitude/10)
            self.x=self.x +dx
            self.y=self.y +dy


# Fonction qui prend en compte les deux fonctions précédentes en fonction de présence ou non d'isolement et de non_respect au confinement
    def deplacement (self,amplitude,isolement,non_respect):
        if isolement:
            if self.statut=="sain" or self.statut=="retabli":
                self.deplacement_normal (amplitude)
            else:
                self.deplacement_isolement (amplitude)
        if non_respect:
            if self.respect=="oui":
                self.deplacement_isolement (amplitude)
            else:
                self.deplacement_normal (amplitude)
        else:
            self.deplacement_normal(amplitude)


#Renvoie la distance euclidienne entre 2 individus
    def distance (self,individu):
        return ((self.x - individu.x)**2 + (self.y - individu.y)**2)**(1/2)


#Dans le cas d'une contamination, il s'agit de savoir à quel degré la personne sera malade et pour combien de temps. Les chiffres choisis représentent une moyenne de temps et de probabilité pour le covid-19 en Europe
    def contamination(self,proba_contamination):
        x=rd.random()
        y=rd.random()
        if x<=proba_contamination:
            if y<=0.78:
                self.statut="asymptomatique"
                self.temps_infection=14
            elif y<=0.95:
                self.statut="malade"
                self.temps_infection=21
            else:
                self.statut="malade critique"
                self.temps_infection=21