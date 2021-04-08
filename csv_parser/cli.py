"""
Cli entrypoint
"""
import os
from file_handler import download_page, name_files, write_file, file_exist


lien = 'https://people.sc.fsu.edu/~jburkardt/data/csv/'
urls = [lien + 'addresses.csv', lien + 'airtravel.csv',
        lien + 'biostats.csv', lien + "cities.csv", ]
for url in urls:
    response = download_page(url)
    name_file = name_files(url)
    print(name_file)
    if not file_exist(name_file):
        write_file(name_file, response)
    else:
        print("le fichier existe deja")   
   


    
