import turtle
import json


def sauvegarder_parametres(taille_carre, taille_grille, debut_x, debut_y):
    parametres = {
        "taille_carre": taille_carre,
        "taille_grille": taille_grille,
        "debut_x": debut_x,
        "debut_y": debut_y,
        "points": []
    }
    
    with open("parametres_et_points.json", "w") as json_file:
        json.dump(parametres, json_file, indent=4)
        print("Paramètres sauvegardés dans parametres_et_points.json")

# Fonction pour sauvegarder les points dans le fichier JSON
def sauvegarder_points(points):
    # Chargez les paramètres existants depuis le fichier JSON s'il existe
    try:
        with open("parametres_et_points.json", "r") as json_file:
            parametres_existants = json.load(json_file)
    except FileNotFoundError:
        parametres_existants = {}

    # Ajoutez les points aux paramètres existants
    parametres_existants["points"] += points

    # Sauvegardez les paramètres mis à jour dans le fichier JSON
    with open("parametres_et_points.json", "w") as json_file:
        json.dump(parametres_existants, json_file, indent=4)
        print("Points sauvegardés dans parametres_et_points.json")
# Sauvegardez les paramètres