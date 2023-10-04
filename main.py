# les fonction importée sont : verifier_clic, colorier_carre
from composent.click import *
# les fonction importée sont : initialiser_grille
from composent.initialization_view import *
# les fonction importée sont : dessiner_carre
from composent.turtle_dessin import *
# les fonction importée sont : sauvegarder_points, sauvegarder_parametres
from composent.sauvegarde import *

import turtle


def main():
    window = turtle.Screen()
    window.setup(width=800, height=800)
    turtle.speed(0)
    taille_carre = 10
    taille_grille = 21
    debut_x = -200
    debut_y = -200
    turtle.goto(debut_x, debut_y)
    while True:
        print("1) Sauvegarder les parametre")
        print("2) lancer le jeu")
        print("9) Break")
        choix = 2
        # int(input(">"))
        if choix == 1:
            sauvegarder_parametres(
                taille_carre, taille_grille, debut_x, debut_y)
        elif choix == 2:
            initialiser_grille(taille_grille, taille_carre)
            window.onclick(lambda x, y: verifier_clic(
                x, y, debut_x, debut_y, taille_carre, taille_grille))
            turtle.done()
        elif choix == 9:
            break


main()
