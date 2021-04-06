"""
Package CSV Parser
"""
import os # imporetr la biblioteque os pour gerer la pause a la fin de script
import requests # importer la bibliotheque request pour charger page et la stocker dans une variable
from requests.exceptions import HTTPError
import urllib.request
from os import getcwd, chdir, mkdir
from os import chdir
import os
rep_cour = os.getcwd()
print(rep_cour)
chdir("csv_uploads")
rep_cour = os.getcwd()
print(rep_cour)

# recuprer la page avec request.get qui lance une requete (http/https)
lien = 'https://people.sc.fsu.edu/~jburkardt/data/csv/'
for url in [lien + 'addresses.csv', lien + 'airtravel.csv',lien + 'biostats.csv', lien + "cities.csv"]:
    try:
        # telecharegr le fichier et le stocker dans 
        chaine = url.split("/")
        name_file = chaine[len(chaine) - 1]        
        if os.path.isfile(name_file):
            print('le fichier existe ')
            
        else:
            print('le fichier n existe pas')
            with open(name_file, 'wb') as file:
                # get request
                response = requests.get(url)  # response est un objet qui permet d'inspecter le resultat de la requete 
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

