import numpy as np
import random as rd
import matplotlib.pyplot as plt
from celluloid import Camera
from simul.personnes import *
from simul.simulation import *
from simul.fonctions import *
from simul.scenarios import *



# Les paramètres ont été choisis conformément aux chiffres révélés sur la pandémie de Covid-19 en Europe. Ces paramètres peuvent être ajustés à toute épidémie. Pour les moyennes, nous avons procédé à une moyenne sur 100 simulations.


# SCENARIO 1 : Aucune mesure
# taille = 100 personnes
# population initialement contaminée : 5%
# population dissidente au confinement : 0%
# distance maximale de contagion : 5
# probabilité de contamination s'il y a contagion : 80%
# amplitude de déplacement : 10
# jours de simulation : 60
# isolement : non
# non_respect du confinement : non

if __name__ == '__main__':
    scenario_simulation (100,0.05,0,5,0.8,10,60,False,False)
    scenario_graphique_moyenne (100,100,0.05,0,5,0.8,10,60,False,False)
    scenario_R0_moyenne (100,100,0.05,0,5,0.8,10,60,False,False)