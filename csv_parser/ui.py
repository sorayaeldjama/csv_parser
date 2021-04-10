"""
User  Interface module.
"""


from cli import download


#  ui.py -> user interface
#  gui.py -> graphical user interface
print("voici notre menu selectionnez l'annalyse que vous souhaiter")
print("fichier 1 a parser")
fichier1 = input("tapez  addresses pour parser le fichier 1")
download(fichier1)
input("tapez cities pour parser le fichier cities")

print("Fichier 2 a parser")
print("Fichier 3 a parser")
