""" Scenarios executant et affichant les simulations """


import numpy as np
import random as rd
import matplotlib.pyplot as plt
from celluloid import Camera
from simul.personnes import *
from simul.simulation import *
from simul.fonctions import *



# Simulation des individus en fonction du temps
def scenario_simulation(taille,p_contamine,p_dissident,d_contagion,p_contamination, amplitude,jours,isolement,non_respect):
    fig=plt.figure()
    camera= Camera(fig)
    simul=initialisation_simulation (taille,p_contamine,p_dissident,d_contagion, p_contamination)
    for individu in simul.population:
        representation(individu)
    camera.snap()
    for j in range(jours):
        iteration_simulation (simul,amplitude,d_contagion,p_contamination,isolement, non_respect)
        for individu in simul.population:
            representation(individu)
        camera.snap()
    animation=camera.animate()
    plt.show()



# Graphique des statistiques de la situation sanitaire en fonction du temps
def scenario_graphique (taille, p_contamine, p_dissident, d_contagion, p_contamination, amplitude, jours, isolement, non_respect):
    simul=initialisation_simulation (taille,p_contamine,p_dissident,d_contagion,p_contamination)
    nb_sain,nb_asymptomatique,nb_malade,nb_malade_critique,nb_mort,nb_retabli,nb_contamine=simul.statistique()
    Sain=[nb_sain]
    Asymptomatique=[nb_asymptomatique]
    Malade=[nb_malade]
    Malade_critique=[nb_malade_critique]
    Mort=[nb_mort]
    Retabli=[nb_retabli]
    Contamine=[nb_contamine]
    for j in range(jours):
        iteration_simulation(simul,amplitude,d_contagion,p_contamination,isolement,non_respect)
        nb_sain,nb_asymptomatique,nb_malade,nb_malade_critique,nb_mort,nb_retabli,nb_contamine=simul.statistique()
        Sain.append(nb_sain)
        Asymptomatique.append(nb_asymptomatique)
        Malade.append(nb_malade)
        Malade_critique.append(nb_malade_critique)
        Mort.append(nb_mort)
        Retabli.append(nb_retabli)
        Contamine.append(nb_contamine)

    fig=plt.figure()
    camera= Camera(fig)
    Jours=[k for k in range(0,jours+1)]
    for j in range (1,jours+2):
        plt.plot(Jours[:j],Sain[:j],label="Sains",color='green')
        plt.plot(Jours[:j],Asymptomatique[:j],label="Asymptomatiques",color='lightsalmon')
        plt.plot(Jours[:j],Malade[:j],label="Malades",color='tomato')
        plt.plot(Jours[:j],Malade_critique[:j],label="Malades critiques",color='r')
        plt.plot(Jours[:j],Mort[:j],label="Morts",color='k')
        plt.plot(Jours[:j],Retabli[:j],label="Rétablis",color='slateblue')
        plt.plot(Jours[:j],Contamine[:j],label="Contaminés",color='gold')
        camera.snap()
    animation=camera.animate()
    plt.show()



# Graphique qui fait la moyenne sur plusieurs simulations
def scenario_graphique_moyenne (nb_simulations, taille, p_contamine, p_dissident, d_contagion, p_contamination, amplitude, jours, isolement, non_respect):
    S=jours*[0]
    A=jours*[0]
    M=jours*[0]
    Mc=jours*[0]
    Mo=jours*[0]
    Re=jours*[0]
    C=jours*[0]
    for _ in range(nb_simulations):
        simul=initialisation_simulation (taille,p_contamine,p_dissident,d_contagion,p_contamination)
        nb_sain,nb_asymptomatique,nb_malade,nb_malade_critique,nb_mort,nb_retabli,nb_contamine=simul.statistique()
        Sain=[nb_sain]
        Asymptomatique=[nb_asymptomatique]
        Malade=[nb_malade]
        Malade_critique=[nb_malade_critique]
        Mort=[nb_mort]
        Retabli=[nb_retabli]
        Contamine=[nb_contamine]
        S[0]+=Sain[0]
        A[0]+=Asymptomatique[0]
        M[0]+=Malade[0]
        Mc[0]+=Malade_critique[0]
        Mo[0]+=Mort[0]
        Re[0]+=Retabli[0]
        C[0]+=Contamine[0]
        for j in range(jours):
            iteration_simulation(simul,amplitude,d_contagion,p_contamination,isolement,non_respect)
            nb_sain,nb_asymptomatique,nb_malade,nb_malade_critique,nb_mort,nb_retabli,nb_contamine=simul.statistique()
            Sain.append(nb_sain)
            Asymptomatique.append(nb_asymptomatique)
            Malade.append(nb_malade)
            Malade_critique.append(nb_malade_critique)
            Mort.append(nb_mort)
            Retabli.append(nb_retabli)
            Contamine.append(nb_contamine)
            S[j]+=Sain[j]
            A[j]+=Asymptomatique[j]
            M[j]+=Malade[j]
            Mc[j]+=Malade_critique[j]
            Mo[j]+=Mort[j]
            Re[j]+=Retabli[j]
            C[j]+=Contamine[j]
    for j in range (jours):
        S[j]=Sain[j]/nb_simulations
        A[j]=Asymptomatique[j]/nb_simulations
        M[j]=Malade[j]/nb_simulations
        Mc[j]=Malade_critique[j]/nb_simulations
        Mo[j]=Mort[j]/nb_simulations
        Re[j]=Retabli[j]/nb_simulations
        C[j]=Contamine[j]/nb_simulations

    fig=plt.figure()
    camera= Camera(fig)
    Jours=[k for k in range(0,jours+1)]
    for j in range (1,jours+1):
        plt.plot(Jours[:j],S[:j],label="Sains",color='green')
        plt.plot(Jours[:j],A[:j],label="Asymptomatiques",color='lightsalmon')
        plt.plot(Jours[:j],M[:j],label="Malades",color='tomato')
        plt.plot(Jours[:j],Mc[:j],label="Malades critiques",color='r')
        plt.plot(Jours[:j],Mo[:j],label="Morts",color='k')
        plt.plot(Jours[:j],Re[:j],label="Rétablis",color='slateblue')
        plt.plot(Jours[:j],C[:j],label="Contaminés",color='gold')
        camera.snap()
    animation=camera.animate()
    plt.show()



# Graphique qui fait la moyenne de R0 sur plusieurs simulations
def scenario_R0 (taille, p_contamine, p_dissident, d_contagion, p_contamination, amplitude, jours, isolement, non_respect):
    simul=initialisation_simulation (taille,p_contamine,p_dissident,d_contagion,p_contamination)
    R0=[simul.r0()]
    for j in range(jours):
        iteration_simulation(simul,amplitude,d_contagion,p_contamination,isolement,non_respect)
        R0.append(simul.r0())

    fig=plt.figure()
    camera= Camera(fig)
    Jours=[k for k in range(0,jours+1)]
    for j in range (1,jours+2):
        plt.plot(Jours[:j],R0[:j],label="Contaminés",color='gold')
        camera.snap()
    animation=camera.animate()
    plt.show()



# Graphique du R0 en fonction du temps
def scenario_R0_moyenne (nb_simulations, taille, p_contamine, p_dissident, d_contagion, p_contamination, amplitude, jours, isolement, non_respect):
    R_moy=jours*[0]
    for _ in range (nb_simulations):
        simul=initialisation_simulation (taille,p_contamine,p_dissident,d_contagion,p_contamination)
        R0=[simul.r0()]
        R_moy[0]+=R0[0]
        for j in range(jours):
            iteration_simulation(simul,amplitude,d_contagion,p_contamination,isolement,non_respect)
            R0.append(simul.r0())
            R_moy[j]+=R0[j]
    for j in range (jours):
        R_moy[j]=R_moy[j]/nb_simulations


    fig=plt.figure()
    camera= Camera(fig)
    Jours=[k for k in range(0,jours+1)]
    for j in range (2,jours+1):
        plt.plot(Jours[:j],R_moy[:j],label="Contaminés",color='gold')
        camera.snap()
    animation=camera.animate()
    plt.show()