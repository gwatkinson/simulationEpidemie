"""Tests unitaires"""


import unittest
import numpy as np
import random as rd
from simul.personnes import Personne
from simul.simulation import Simulation
from simul.fonctions import initialisation_individu_sain, initialisation_individu_contamine


class TestSimulation(unittest.TestCase):

    def testCoordonees(self):
        """ Test si les coordonnées de pers respecte bien les conditions du modèle """
        pers = initialisation_individu_sain()
        self.assertIsInstance(pers.x, float)
        self.assertIsInstance(pers.y, float)
        self.assertTrue(0 <= pers.x <= 100)
        self.assertTrue(0 <= pers.y <= 100)


    def testDeplacement_normal(self):
        """ Test la fonction deplacement_normal """
        pers = initialisation_individu_sain()
        pers.deplacement_normal(10)
        pers.deplacement_normal(10)
        x,y = pers.x, pers.y
        pers.deplacement_normal(10)
        self.assertTrue(np.abs(x-pers.x) < 10)
        self.assertTrue(np.abs(y-pers.y) < 10)


    def testDistance(self):
        """ Test si la fonction distance renvoie la bonne valeur dans ce cas """
        pers3 = Personne(x=1,y=4)
        pers4 = Personne(x=1,y=2)
        self.assertEqual(pers3.distance(pers4), 2)


    def testStatut(self):
        """ Test le format du statut de pers et de pers2 """
        pers = initialisation_individu_sain()
        pers2 = initialisation_individu_contamine()
        self.assertEqual(pers.statut, "sain")
        self.assertIn(pers2.statut, ["asymptomatique", "malade", "malade critique"])


    def testTempsInfection(self):
        """ Test si temps_infection respecte bien les conditions du modèle """
        pers = initialisation_individu_sain()
        pers2 = initialisation_individu_contamine()
        self.assertIn(pers2.temps_infection, [15, 22])
        self.assertEqual(pers.temps_infection, 0)


    def testInitSimulation(self):
        """ Test la fonction __init__ de la classe Simulation """
        pers = initialisation_individu_sain()
        pers2 = initialisation_individu_contamine()
        self.simulation = Simulation(population=[pers, pers2])
        self.assertIsInstance(self.simulation.population, list)
        self.assertEqual(len(self.simulation.population), 2)
        self.assertIsInstance(self.simulation.population[0], Personne)
        self.assertIsInstance(self.simulation.proba_contamination, float)
        self.assertTrue(0 <= self.simulation.proba_contamination <= 1)



if __name__ == '__main__':
    unittest.main()