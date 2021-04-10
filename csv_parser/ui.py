"""
User  Interface module.
"""


from cli import download, afficher


#  ui.py -> user interface
#  gui.py -> graphical user interface
lien = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
print("voici notre menu selectionnez l'annalyse que vous souhaiter")
print("fichier 1 a parser")
fichier1 = input("tapez  addresses pour parser le fichier 1")
download(fichier1)
afficher1 = input("tapper 1 pour afficher le fichier addresses")
afficher(fichier1)

fichier2 = input("tapez cities pour parser le fichier cities")
download(fichier2)


print("Fichier 2 a parser")
print("Fichier 3 a parser")
