# les fonction importée sont : verifier_clic, colorier_carre
from composent.click import * 
# les fonction importée sont : initialiser_grille
from composent.initialization_view import *
# les fonction importée sont : dessiner_carre 
from composent.turtle_dessin import *
# les fonction importée sont : sauvegarder_points, sauvegarder_parametres
from composent.sauvegarde import *

import turtle

def ajouter_carre(x, y, taille_carre):
    dessiner_carre(taille_carre, x, y, "black")



if __name__ == "__main__":
    window = turtle.Screen()
    turtle.speed(0)
    taille_carre = 10
    taille_grille = 15
    debut_x = 0
    debut_y = 0
    while True:
        print("1) Sauvegarder les parametre")
        print("2) lancer le jeu")
        choix = int(input(">"))
        if choix == 1:    
            sauvegarder_parametres(taille_carre, taille_grille, debut_x, debut_y)
        elif choix == 2:
            initialiser_grille(taille_grille, taille_carre)
            window.onclick(lambda x, y: verifier_clic(x, y, debut_x, debut_y, taille_carre, taille_grille))
            turtle.done()


