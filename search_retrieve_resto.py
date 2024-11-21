import requests
import json
""" import argparse

parser = argparse.ArgumentParser(description="Script pour les recherches (SIRET, SIRET et CA)") # Instance de argparse
parser.add_argument('--resto', default="",  help="") # Instance de argparse """

def search_by_siret(siret):
    # URL de l'API pour la recherche par SIRET
    BASE_URL = "https://data.siren-api.fr/v3/etablissements/"

    # Clé API
    API_KEY = "RuFLHcgw2ZW5778hqWmLYHhMIJ8CC0dl"  # Remplacez par None si la clé n'est pas requise

    # Headers pour la requête
    headers = {
        "Accept": "application/json",        # Demande une réponse en JSON
        "X-Client-Secret": API_KEY          # Clé API dans l'en-tête
    }

    if API_KEY:  # Si une clé API est fournie
        headers["Authorization"] = f"Bearer {API_KEY}"

    # Envoi de la requête GET
    try:
        response = requests.get(f"{BASE_URL}{siret}", headers=headers)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()  # Convertit la réponse en JSON
        formatted_data = json.dumps(data, indent=2, sort_keys=True)
        print("Données récupérées :")
        print(formatted_data)
    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel API :", e)
    return data 

def siret_to_ca(rest_name, code_postal):
    # URL de l'API
    BASE_URL = "https://recherche-entreprises.api.gouv.fr/search"

    # Paramètres de la requête
    params = {
        "q": rest_name,  # Recherche par mot-clé
        "code_postal": code_postal  # Filtre par code postal
    }

    # Clé API (à remplacer par votre clé, si nécessaire)
    API_KEY = "eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjoiNjczZWY0NmMxY2Y3ODZmOWM0YTE3YjcwIiwidGltZSI6MTczMjE3OTA4NC40MzU3NDI0fQ.9ZKleEb3xVhIxWHiKqUVKiZxQUMfpGa1lfpgkZrMmPjsK8-iSNLPSCK_Wu-tNz_roBrgy04SqTSM2lGSuuMYRg"

    # Headers pour la requête
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # En-tête avec la clé API
    }

    # Envoi de la requête GET
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Vérifie les erreurs HTTP

        # Conversion en JSON
        data = response.json()

        # Affichage formaté du JSON
        formatted_data = json.dumps(data, indent=2, sort_keys=True)
        print("Données récupérées :")
        print(formatted_data)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel API :", e)


# Exemple d'appel à la fonction
search_by_siret("40118227400019")
