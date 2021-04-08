"""
Package CSV Parser
"""
import os  
import requests 
from requests.exceptions import HTTPError
from os import getcwd, chdir  

"""
rep_cour = getcwd()  # connaitre notre repertoire actuel
print(rep_cour)
chdir("csv_uploads")
rep_cour = os.getcwd()
print(rep_cour)
"""


def download_page(url):
    # Telacharger la page csv
    try:
        response = requests.get(url)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')   
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!, le lien est telecharger')


def name_file(url):
    chaine = url.split("/")
    name_file = chaine[len(chaine) - 1]        


def write_file(response):
    with open(name_file, 'wb') as file:
        # write to file
        file.write(response.content)
        # si response est successful, no Exception will be raised 
        response.raise_for_status()  # un HTTPErrorsera déclenché pour certains codes d'état


def file_exist():
    if os.path.isfile(name_file):
        print('le fichier existe ')            
