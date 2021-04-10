"""
Cli entrypoint
"""
import os, csv
from file_handler import download_page, name_files, write_file, file_exist


lien = 'https://people.sc.fsu.edu/~jburkardt/data/csv/'
# urls = [lien + 'addresses.csv', lien + 'airtravel.csv',
#  lien + 'biostats.csv', lien + "cities.csv", ]
# for url in urls:


def download(fichier):
    response = download_page(lien + fichier + ".csv")
    name_file = name_files(lien + fichier + ".csv")
    print(name_file)
    if not file_exist(name_file):
        write_file(name_file, response)
    else:
        print("le fichier existe deja")


def afficher(fichier):
    path = os.getcwd()
    f = open(path + "\\csv_uploads\\" + fichier + ".csv")
    myReader = csv.reader(f)
    for row in myReader:
        print(row)
  

