from tkinter import *
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
import tkinter as tk

import self

import RecconaisanceFaciale
from RecconaisanceFaciale import FaceDetector

import cv2
#from matplotlib import pyplot as plt

from tkinter import messagebox
import tkinter as tk
from numpy import can_cast

root = Tk()
root.title("Paint App")
root.geometry("1500x1500")
cadre = Frame(root, height=100, width=900, bg ="green")
cadre.grid(row=0, column=1)

def Reconnaissancef():
    FaceDetector.start_detection(self)


def pinceaux():
    couleurinitial.set("black")
    canvas["cursor"] = "arrow"

def effacer():
    couleurinitial.set("white")
    canvas["cursor"] = DOTBOX

def choisir_la_couleur():
    choisir_la_couleur =colorchooser.askcolor()
    couleurinitial.set(choisir_la_couleur[1])

    if choisir_la_couleur[1]== None:
        couleurinitial.set("black")

def Jaune():
    couleurinitial.set("yellow")

def Rouge():
    couleurinitial.set("red")

def enregistrer():
    localisationfichier =filedialog.asksaveasfilename(defaultextension="jpg")
    x = root.winfo_rootx()
    y =root.winfo_rooty()+100
    image = ImageGrab.grab(bbox=(x, y, x+1100,y+500))
    image.show()
    image.save(localisationfichier)

def chargerimage():
    # Chemin vers l'image
    chemin_image = "E:\image.jpg"
    # Charger l'image avec OpenCV
    image = cv2.imread(chemin_image)

    # Vérifier si l'image est chargée correctement
    if image is not None:
        # Afficher des informations sur l'image (dimensions, type de données)
        print(f"Dimensions de l'image : {image.shape}")
        print(f"Type de données de l'image : {image.dtype}")

        # Afficher l'image (utilisation d'une fenêtre OpenCV)
        cv2.imshow("Image chargée avec OpenCV", image)
        cv2.waitKey(0)  # Attendre une touche
        cv2.destroyAllWindows()  # Fermer la fenêtre
    else:
        print(f"Impossible de charger l'image à partir de {chemin_image}")

    canvas.bind("<B1-Motion>", dessiner)
    canvas.bind("<ButtonRelease-1>", dessiner)


#difinitions de tous mes boutons

elementcadre = Frame(root, height=600, width=200, bg ="black")
elementcadre.grid(row=0, column=0, sticky="NW")

fichier= Button(elementcadre, text= "Fichier")
fichier.grid(row =0 ,column=0)

Acceuil = Button(elementcadre, text= "Acceuil")
Acceuil.grid(row =0 ,column=1)

Affichage = Button(elementcadre, text= "Affichage")
Affichage.grid(row =0 ,column=2)

cadre2 = Frame(root,height=600, width=900, bg ="yellow")
cadre2.grid(row=1, column=1)

cadre1 = Frame(root,height=600, width=250, bg ="blue")
cadre1.grid(row=1, column=2)

cadre4 = Frame(root,height=600, width=250, bg ="blue")
cadre4.grid(row=1, column=0)

#elements du cadre4 c'esr à dire 1er cadre
elementcadre2 = Frame(root, height=600, width=200)
elementcadre2.grid(row=1, column=0, sticky="NW")

dessiner = Button(elementcadre2, text= "Pinceau", height=3, width=7, padx=13, command=pinceaux)
dessiner.grid(row=2, column=1)

ajuster= Button(elementcadre2, text= "Ajuster", height=3, width=7, padx=13)
ajuster.grid(row=2, column=2)

effacer= Button(elementcadre2, text= "Effacer", height=3, width=7, padx=13, command=effacer)
effacer.grid(row=2, column=3)

agrandir = Button(elementcadre2, text= "Zoom", height=3, width=7, padx=13)
agrandir.grid(row=3, column=3)

loupe = Button(elementcadre2, text= "Loupe", height=3, width=7, padx=13)
loupe.grid(row=3, column=1)

ecrire = Button(elementcadre2, text= "Ecrire", height=3, width=7, padx=13)
ecrire.grid(row=3, column=2)

forme = Button(elementcadre2, text= "Forme", height=3, width=7, padx=13)
forme.grid(row=4, column=2)

forme = Button(elementcadre2, text= "Forme", height=3, width=7, padx=13)
forme.grid(row=4, column=2)

#bouton couleurs
couleurs = Button(elementcadre2, text= "Couleurs", height=3, width=7, padx=13, bg = "white",command=choisir_la_couleur)
couleurs.grid(row=5, column=1)

elements = Button(elementcadre2, text= "Base", height=3, width=7, padx=13)
elements.grid(row=7, column=2)

jaune = Button(elementcadre2, height=1, width=2, padx=13, bg= "yellow", command=Jaune)
jaune.grid(row=5, column=2)

rouge = Button(elementcadre2, height=1, width=2, padx=13, bg= "red", command=Rouge)
rouge.grid(row=5, column=3)

vert = Button(elementcadre2, height=1, width=2, padx=13, bg= "green", command=lambda :couleurinitial.set("green"))
vert.grid(row=6, column=2)

bleue = Button(elementcadre2, height=1, width=2, padx=13, bg= "blue", command=lambda :couleurinitial.set("blue"))
bleue.grid(row=6, column=3)

save = Button(elementcadre2, text= "Enregister", height=3, width=7, padx=13, command =enregistrer)
save.grid(row=8, column=2)

elementcadre3 = Frame(root, height=600, width=200)
elementcadre3.grid(row=1, column=2, sticky="NW")

charger = Button(elementcadre3, text="Charger_iMAGE", height=3, width=10, padx=13, command =chargerimage)
charger.grid(row=1, column=1)

reconnaissanceFaciale = Button(elementcadre3, text="Reconnaisance faciale", height=3, width=10, padx=13, command= Reconnaissancef)
reconnaissanceFaciale.grid(row=2, column=1)





ajusterpinceau = IntVar()
ajusterpinceau.set(1)

options = [1,2,3,4,5]

menuechoix = OptionMenu(ajuster, ajusterpinceau, *options)
menuechoix.grid(row=2, column=2)


#définir mon cadre de dessin
canvas = Canvas(cadre2, height=600, width=900, bg ="white")
canvas.grid(row=1, column=1)
couleurinitial = StringVar()
couleurinitial.set("green")

#innitialisation du curseur de dessin
pointprecedent = [0, 0]
pointsuivant = [0, 0]


def dessiner(position):
    print(position.type)
    global pointprecedent
    global pointsuivant
    x = position.x
    y = position.y
    pointsuivant = [x, y]

    #ligne sans inter
    if pointprecedent != [0, 0]:
        canvas.create_line(pointprecedent[0], pointprecedent[1], pointsuivant[0], pointsuivant[1], fill=couleurinitial.get(),width=ajusterpinceau.get())

    pointprecedent= pointsuivant

    if dessiner.type == "5":
        pointprecedent = [0, 0]

# Charger l'image avec OpenCV



root.resizable(True,False)
root.mainloop()



