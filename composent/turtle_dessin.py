
import turtle
import json


def dessiner_carre(taille_carre, x, y, couleur_remplissage):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(couleur_remplissage)
    turtle.begin_fill()
    for _ in range(4):
        turtle.left(90)
        turtle.forward(taille_carre)
    turtle.end_fill()
