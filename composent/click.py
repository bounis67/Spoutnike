
from composent.click import *
from composent.initialization_view import *
from composent.turtle_dessin import *
from composent.sauvegarde import *
from main import *

import turtle
import json


def ajouter_carre(x, y, taille_carre):
    dessiner_carre(taille_carre, x, y, "black")


def verifier_clic(x, y, debut_x, debut_y, taille_carre, taille_grille):
    debut_grille_x = debut_x
    debut_grille_y = debut_y
    fin_grille_x = debut_x + taille_carre * taille_grille
    fin_grille_y = debut_y + taille_carre * taille_grille
    if debut_grille_x < x < fin_grille_x and debut_grille_y < y < fin_grille_y:
        print(
            f"Souris cliquée aux coordonnées ({x}, {y}) à l'intérieur de la grille.")
        position_x_clic = int(((x - debut_grille_x) / taille_carre))
        position_y_clic = int(((y - debut_grille_y) / taille_carre) + 1)
        print("Cliqué à la ligne", position_y_clic)

        position_x_carre = (
            ((position_x_clic * taille_carre)) + debut_grille_x)
        position_y_carre = (
            ((position_y_clic * taille_carre)) + debut_grille_y)
        print("position_x_carre", position_x_carre,
              "position_y_carre", position_y_carre)
        ajouter_carre(position_x_carre, position_y_carre, taille_carre)
        nouveaux_points = [{"x": position_x_carre, "y": position_y_carre}]
        sauvegarder_points(nouveaux_points)
    else:
        print(
            f"Souris cliquée aux coordonnées ({x}, {y}) à l'extérieur de la grille.")
