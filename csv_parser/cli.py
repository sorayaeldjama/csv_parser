"""
Cli entrypoint
"""
from file_handler import download_page, name_file, write_file, file_exist


lien = 'https://people.sc.fsu.edu/~jburkardt/data/csv/'
urls = [lien + 'addresses.csv', lien + 'airtravel.csv',
        lien + 'biostats.csv', lien + "cities.csv", ]
for url in urls:
    download_page(url)  
    
