""" Classe Simulation pour créer les individus de la simulation """


import numpy as np
import random as rd
import matplotlib.pyplot as plt
from simul.personnes import *



class Simulation:

    def __init__(self,**kwargs):
        self.population=kwargs.get("population",[])
        self.pourcentage_initial_infecte=kwargs.get("pourcentage_initial_contamine",0.05)
        self.distance_contagion=kwargs.get("distance_contagion",3)
        self.proba_contamination=kwargs.get("proba_contamination",0.8)


# Renvoie les statistiques à un moment donné de la situation sanitaire
    def statistique (self):
        nb_sain=0
        nb_asymptomatique=0
        nb_malade=0
        nb_malade_critique=0
        nb_mort=0
        nb_retabli=0
        for individu in self.population:
            if individu.statut=="sain":
                nb_sain+=1
            elif individu.statut=="asymptomatique":
                nb_asymptomatique+=1
            elif individu.statut=="malade":
                nb_malade+=1
            elif individu.statut=="malade critique":
                nb_malade_critique+=1
            elif individu.statut=="mort":
                nb_mort+=1
            elif individu.statut=="retabli":
                nb_retabli+=1
        nb_contamine=nb_asymptomatique + nb_malade + nb_malade_critique
        return nb_sain, nb_asymptomatique, nb_malade, nb_malade_critique, nb_mort, nb_retabli, nb_contamine


#renvoie le R0 à un moment donné de la crise sanitaire
    def r0 (self):
        L=[]
        for individu in self.population:
            if individu.statut in ("asymptomatique","malade","malade critique"):
                c=0
                for individu2 in self.population:
                    if individu2.statut == "sain" and individu.distance(individu2)<=self.distance_contagion:
                        c+=1
                L.append(c)
        if len(L)>0:
            return sum(L)/len(L) * (1/self.proba_contamination)
        return 0