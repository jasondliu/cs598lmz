import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("Pokemon Terminal Trainer by TheHappieCat")

#Imports the stuffs we need
import sys
import random
import os
import time

#Sets all the auto variables

StartingPokemon = 1
#Used to determain if the player lost/won.
GameState = 0
#Sets the player's current pokemon
CurrentPokemon = 0
#Sets the number of pokemon the player has.
PokemonCount = 0
#Used to switch between using the player's move or the AI's move
PlayerTurn = 0
#Used to see if the health of a pokemon was changed this turn.
HealthChanged = 0
#Used to seed the RNG
RNGseed = 0

#The pokemon class, contains all the information of a pokemon
class Pokemon:
    def __init__(self, Name, Number, Ability, Health, Attack, Defense, Speed, Move1, Move2, Move3, Move4, Type1 = "None", Type2 = "None", CatchRate = 0, Exp = 0):
        self.Name = Name
        self.Number = Number
        self.
