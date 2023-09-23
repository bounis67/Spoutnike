import turtle
import json



def initialiser_grille(taille_grille, taille_carre):
    for _ in range(2):
        for _ in range(taille_grille):
            turtle.forward(taille_carre * taille_grille)
            if _ % 2 == 0:
                turtle.left(90)
                turtle.forward(taille_carre)
                turtle.left(90)
            else:
                turtle.right(90)
                turtle.forward(taille_carre)
                turtle.right(90)
        turtle.forward(taille_carre * taille_grille)
        turtle.left(90)


