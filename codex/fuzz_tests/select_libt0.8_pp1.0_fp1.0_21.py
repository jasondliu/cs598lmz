import selected as selected
import map_ui as ui
import tkinter as tk
import import_images
import map_ui
import forces
import globals
import math
import copy
import tkinter.filedialog
import tkinter.messagebox
import io
import tkinter.font
import colorsys
import PIL
import PIL.Image, PIL.ImageTk
import tkinter.colorchooser
import json

class Map:
    def __init__(self, app, **kwargs):
        self.name = "Map 1"
        self.scale = 1
        self.scale_adjustment = 0
        self.window_offset = [0, 0]
        self.dragging = False
        self.player_start = [100, 100]
        self.number_of_players = 4
        self.players = []
        self.app = app
        self.show_grid = False
        self.show_player_paths = True
        self.show_vision_paths = True
        self.show_select_rectangle = True
       
