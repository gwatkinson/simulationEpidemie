""" Fonctions permettant d'executer la simulation """


import numpy as np
import random as rd
import matplotlib.pyplot as plt
from simul.personnes import *
from simul.simulation import *



def initialisation_individu_sain():
    a=rd.random()*100
    b=rd.random()*100
    return Personne(x=a,y=b)


def initialisation_individu_contamine():
    a=rd.random()*100
    b=rd.random()*100
    y=rd.random()
    if y<=0.78:
        s="asymptomatique"
        t=15
    elif y<=0.95:
        s="malade"
        t=22
    else:
        s="malade critique"
        t=22
    return Personne(x=a,y=b,statut=s,temps_infection=t)


def initialisation_individu_dissident():
    a=rd.random()*100
    b=rd.random()*100
    return Personne(x=a,y=b,respect="non")


# Initialise une simulation avec les paramètres d'entrée.
# taille : taille de l'échantillon
# p_contamine : proportion dans l'échantillon initialement contaminé
# p_dissident : proportion dans l'échantillon qui sont dissidents au confinement
# d_contagion : distance maximale de contagion
# p_contamination : probabilité de contamination s'il y a contagion

def initialisation_simulation(taille, p_contamine, p_dissident, d_contagion, p_contamination):
    nb_contamine=int(taille*p_contamine)
    nb_dissident=int(taille*p_dissident)
    pop=[]
    for _ in range(nb_contamine):
        pop.append(initialisation_individu_contamine())
    for _ in range(nb_dissident):
        pop.append(initialisation_individu_dissident())
    for _ in range(taille-nb_contamine-nb_dissident):
        pop.append(initialisation_individu_sain())
    return Simulation(population=pop, pourcentage_initial_contamine=p_contamine, distance_contagion=d_contagion, proba_contamination=p_contamination)


# Itération de la simulation d'un jour au suivant
def iteration_simulation(simul, amplitude, d_contagion, p_contamination, isolement, non_respect):

    for individu in simul.population:
        if individu.statut != "mort":
            individu.deplacement(amplitude,isolement,non_respect)
        if individu.temps_infection>0:
            individu.temps_infection-=1
        if individu.temps_infection==0 and individu.statut=="asymptomatique":
            individu.statut="retabli"
        if individu.temps_infection==0 and individu.statut=="malade":
            r=rd.random()
            if r<0.01:
                individu.statut="mort"
            else:
                individu.statut="retabli"
        if individu.temps_infection==0 and individu.statut=="malade critique":
            r=rd.random()
            if r<0.2:
                individu.statut="mort"
            else:
                individu.statut="retabli"
    liste_contamine=[individu for individu in simul.population if individu.statut not in ("sain","mort","retabli")]
    for individu in simul.population:
            for contamine in liste_contamine:
                if individu.distance(contamine)<= d_contagion and individu.statut=="sain":
                    individu.contamination(p_contamination)


# Représentation graphique de la simulation
def representation (individu):
    x=individu.x
    y=individu.y
    if individu.statut=="sain":
        plt.plot(x,y,marker='o',color='green')
    if individu.statut=="asymptomatique":
        plt.plot(x,y,marker='o',color='lightsalmon')
    if individu.statut=="malade":
        plt.plot(x,y,marker='o',color='tomato')
    if individu.statut=="malade critique":
        plt.plot(x,y,marker='o',color='r')
    if individu.statut=="mort":
        plt.plot(x,y,marker='o',color='k')
    if individu.statut=="retabli":
        plt.plot(x,y,marker='o',color='slateblue')