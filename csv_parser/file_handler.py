"""
Package CSV Parser
"""
import os  
import requests 
from requests.exceptions import HTTPError
from os import getcwd 


def download_page(url):
    # Telacharger la page csv
    try:
        response = requests.get(url)
        #  si response est successful, no Exception will be raised 
        response.raise_for_status()  # un HTTPErrorsera déclenché
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')   
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!, le lien est telecharger')
    return response


def name_files(url):
    chaine = url.split("/")     
    return chaine[len(chaine) - 1]


def write_file(name_file, response):
    path = os.getcwd()
    with open(path + '/csv_uploads/' + name_file, 'wb') as file:
        file.write(response.content)
        

def file_exist(name_file):
    path = os.getcwd()
    try:
        if os.path.isfile(path + '/csv_uploads/' + name_file):              
            print('le fichier existe ') 
        else:
            print("il n existe pas")                 
    except:
        print("le repertoire n existe pas")