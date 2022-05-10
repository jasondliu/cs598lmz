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

class GridWorld:
    def __init__(self, grid_size=10, default_reward=0, terminal_rewards=None, 
                 terminal_states=None, terminal_probability=0.1, stochastic_probability=0.1,
                 stochastic_rewards=None, stochastic_states=None, alpha=0.1, gamma=0
