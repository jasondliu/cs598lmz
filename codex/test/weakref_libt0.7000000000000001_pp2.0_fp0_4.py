import weakref
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from IPython.display import display, clear_output
from copy import copy, deepcopy

from PIL import Image, ImageDraw

def display_image(img):
    display(Image.fromarray(img))

class Cell:
    def __init__(self, x, y, parent=None, value=0, is_terminal=False):
        self.x = x
        self.y = y
        self.parent = parent
        self.value = value
        self.is_terminal = is_terminal

