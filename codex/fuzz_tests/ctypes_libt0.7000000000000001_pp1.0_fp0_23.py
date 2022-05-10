import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Projet SNAKE")

#Import des modules
import sys
import time
import random
import msvcrt

#Variables
snake = [["$",2,2],["@",2,3],["#",2,4]]
pasX = 0
pasY = 0
fin = False
direction = "droite"
psnake = [["$",2,2],["@",2,3],["#",2,4]]
fruit = ["#",random.randint(0,15),random.randint(0,15)]
niveau = 1

#Fonctions
def afficher_titre():
    print("""
 _______  _______  _______  _______  _______  _______  _______ 
(  ____ \(  ____ \(  ____ \(  ___  )(  ____ \(  ____ \(  ____ \\
| (    \/| (    \/| (    \/| (   ) || (    \/| (    \/| (    \
