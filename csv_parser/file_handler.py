# parser un site web
import os # imporetr la biblioteque os pour gerer la pause a la fin de script
import requests # importer la bibliotheque request pour charger page et la stocker dans une variable
from requests.exceptions import HTTPError
import urllib.request

"""
def name_file(url):
    chaine = url.split("/")
    name_file = chaine[len(chaine) - 1]

# fonction pour verifier si le fichier existe deja
def verifier(fileName):
    fileName = r"C:\Users\soray\Documents\cours python\Projets\csv-parser"
    os.path.exists(fileName)

def telecharger():
    # recuprer la page avec request.get qui lance une requete (http/https)
    for url in ['https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv']:
        #name_file = name_file(url)
        #file_exist = verifier(name_file)
        #while not file_exist :
        try:
                # telecharegr le fichier et le stocker dans 
                name_file(url)
                with open(name_file, 'wb') as file:
                    # get request
                    response = requests.get(url) # response est un objet qui permet d'inspecter le resultat de la requete 
                    # write to file
                    file.write(response.content)
                    # si response est successful, no Exception will be raised 
                    response.raise_for_status() # un HTTPErrorsera déclenché pour certains codes d'état si le code d'etat indique reussit il continu 
        except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')   
        except Exception as err:
                print(f'Other error occurred: {err}')  
        else:
                print('Success!') """
   
# recuprer la page avec request.get qui lance une requete (http/https)
for url in ['https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv']:
    try:
        # telecharegr le fichier et le stocker dans 
        chaine = url.split("/")
        name_file = chaine[len(chaine) - 1]
        with open(name_file, 'wb') as file:
            # get request
            response = requests.get(url) # response est un objet qui permet d'inspecter le resultat de la requete 
            # write to file
            file.write(response.content)
            # si response est successful, no Exception will be raised 
            response.raise_for_status() # un HTTPErrorsera déclenché pour certains codes d'état si le code d'etat indique reussit il continu 
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')   
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')

print("hello")