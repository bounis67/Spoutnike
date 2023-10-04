# les fonction importée sont : verifier_clic, colorier_carre
from composent.click import *
# les fonction importée sont : initialiser_grille
from composent.initialization_view import *
# les fonction importée sont : dessiner_carre
from composent.turtle_dessin import *
# les fonction importée sont : sauvegarder_points, sauvegarder_parametres
from composent.sauvegarde import *

from composent.restitution import *

import turtle

<<<<<<< HEAD

def main():
    window = turtle.Screen()
    window.setup(width=800, height=800)
    turtle.speed(0)
    taille_carre = 10
    taille_grille = 21
=======

def ajouter_carre(x, y, taille_carre):
    dessiner_carre(taille_carre, x, y, "black")


def main():
    window = turtle.Screen()
    window.setup(600, 600)
    turtle.speed(0)
    taille_carre = 25
    taille_grille = 15
>>>>>>> 4cf1736be3d9845eefbf7caee7d2f6a99c6968c3
    debut_x = -200
    debut_y = -200
    turtle.goto(debut_x, debut_y)
    while True:
        print("1) Sauvegarder les parametre")
        print("2) lancer le jeu")
<<<<<<< HEAD
        print("9) Break")
        choix = 2
        # int(input(">"))
=======
        print("3) Restituer")
        print("4) Quitter")
        choix = int(input(">"))
>>>>>>> 4cf1736be3d9845eefbf7caee7d2f6a99c6968c3
        if choix == 1:
            sauvegarder_parametres(
                taille_carre, taille_grille, debut_x, debut_y)
        elif choix == 2:
            initialiser_grille(taille_grille, taille_carre)
            window.onclick(lambda x, y: verifier_clic(
                x, y, debut_x, debut_y, taille_carre, taille_grille))
            turtle.done()
<<<<<<< HEAD
        elif choix == 9:
            break


main()
=======
        elif choix == 3:
            restitution()
            window.onclick(lambda x, y: verifier_clic(
                x, y, debut_x, debut_y, taille_carre, taille_grille))
        elif choix == 4:
            break


def restitution():
    try:
        with open("parametres_et_points.json", "r") as json_file:
            json_file = json.load(json_file)
    except FileNotFoundError:
        parametres_existants = {}
    print(json_file["taille_carre"])
    taille_carre = json_file["taille_carre"]
    taille_grille = json_file["taille_grille"]
    debut_x = json_file["debut_x"]
    debut_y = json_file["debut_y"]
    points = json_file["points"]
    initialiser_grille(taille_grille, taille_carre)
    for point in points:
        ajouter_carre(point["x"], point["y"], taille_carre)


if __name__ == "__main__":
    main()
    turtle.done()


# 388fa3
>>>>>>> 4cf1736be3d9845eefbf7caee7d2f6a99c6968c3
