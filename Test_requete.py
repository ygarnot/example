import requests

def obtenir_meteo_toulouse():
    """
    Récupère la météo actuelle à Toulouse en utilisant l'API OpenWeatherMap.
    Vous devez obtenir une clé API gratuite sur le site d'OpenWeatherMap.
    """
    api_key = "VOTRE_CLE_API"  # Remplacez par votre clé API OpenWeatherMap
    ville = "Toulouse"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    langue = "fr"  # Pour obtenir la description en français
    unites = "metric"  # Pour obtenir la température en Celsius

    complete_url = base_url + "appid=" + api_key + "&q=" + ville + "&lang=" + langue + "&units=" + unites

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP

        data = response.json()

        if data["cod"] == 200:
            meteo_principale = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            ressentie = data["main"]["feels_like"]
            humidite = data["main"]["humidity"]
            vitesse_vent = data["wind"].get("speed")  # Utilisation de get pour éviter une erreur si la vitesse du vent n'est pas présente

            print(f"Météo actuelle à Toulouse :")
            print(f"Description : {meteo_principale}")
            print(f"Température : {temperature}°C")
            print(f"Ressentie : {ressentie}°C")
            print(f"Humidité : {humidite}%")
            if vitesse_vent is not None:
                print(f"Vitesse du vent : {vitesse_vent} m/s")
            else:
                print("Informations sur la vitesse du vent non disponibles.")
        else:
            print(f"Erreur lors de la récupération des données météo : {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
    except KeyError as e:
        print(f"Erreur lors de l'analyse des données JSON : Clé manquante - {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    obtenir_meteo_toulouse()
