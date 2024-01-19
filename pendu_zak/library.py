import json
import random

def choisir_mot():
    mots = ["abricot", "ananas", "avocat", "banane", "cassis", "cerise", "citron", "clementine", "datte", "figue",
            "fraise", "framboise", "goyave", "grenade", "groseille", "kiwi", "mangue", "melon", "mirabelle", "myrtille",
            "orange", "pamplemousse", "pasteque", "peche", "poire", "pomme", "prune", "raisin", "rhubarbe", "tangerine",
            "anone", "arbre a pain", "baie", "carambole", "coing", "cranberry", "kaki", "litchi", "mure", "papaye", 
            "rhubarbe", "tomate", "framboise", "mure", "nectarine"]
    mot_aleatoire = random.choice(mots)
    return mot_aleatoire

def changer_mot(nouveau_mot, null):
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Mettre à jour le mot dans les données
    donnees['mots'] = nouveau_mot

    # Écrire les données mises à jour dans le fichier JSON
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=2)

def mot_actuel():
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    return donnees['mots']


def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def afficher_lettres_proposees():
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Vérifier si la clé 'lettres_proposees' existe dans les données
    if 'lettres_proposees' in donnees:
        lettres_proposees = donnees['lettres_proposees']
        return lettres_proposees
    else:
        return []


def vie_actuel():
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    return donnees['vie']        
    
def changer_vie(nombre):
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Mettre à jour le mot dans les données
    donnees['vie'] = nombre

    # Écrire les données mises à jour dans le fichier JSON
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=2)

def afficher_lettres_trouvees():
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Vérifier si la clé 'lettres_trouvees' existe dans les données
    if 'lettres_trouvees' in donnees:
        lettres_trouvees = donnees['lettres_trouvees']
        return lettres_trouvees
    else:
        return []

def ajoute_lettre_trouvees(lettre):
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Ajouter la lettre aux lettres trouvées
    if 'lettres_trouvees' in donnees:
        donnees['lettres_trouvees'].append(lettre)
    else:
        donnees['lettres_trouvees'] = [lettre]

    # Écrire les données mises à jour dans le fichier JSON
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=2)

def reset_lettres_trouvees():
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Réinitialiser les lettres trouvées
    donnees['lettres_trouvees'] = []

    # Écrire les données mises à jour dans le fichier JSON
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=2)

def reset_lettres_proposees():
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    # Réinitialiser les lettres proposées
    donnees['lettres_proposees'] = []

    # Écrire les données mises à jour dans le fichier JSON
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=2)

def get_json():
    # Chemin du fichier JSON
    fichier_json = "./data.json"

    # Charger les données actuelles depuis le fichier JSON
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)

    return donnees
    