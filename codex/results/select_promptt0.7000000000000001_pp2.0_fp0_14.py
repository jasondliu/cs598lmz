import select
# Test select.select, if it fails, use time.sleep
try:
    select.select([], [], [], 0)
except ValueError:
    select.select = lambda *args: ([], [], [])

from tkinter import *
from tkinter.constants import *
from tkinter import ttk

from PIL import Image, ImageDraw

# this is for my own map generator
from MapGenerator import Map

# import constant definitions
from Constants import *

# import game data (items, mobs, etc)
from Items import *
# import game data (items, mobs, etc)
from Mobs import *

# Import game classes
import Game

# Import game actions
import Actions


# import sprites
import Sprites

# Import GUI
import GUI

# Import GUI actions
import GUIActions

# Import GUI dialogs
import Dialogs

# Import GUI character sheet
import CharacterSheet

import SaveLoad


# create the root window, set title
root = Tk()
root.title("Boredom")
root.iconbitmap("icon.
