import types
types.__path__

import os
import sys
from PIL import Image


# Lazy loading of pygame as it has many dependencies.
try:
    import pygame
except ImportError:
    pygame = None
    pass


# This global variable will be used to assign color for the plot
# color_palette = ['#32CD32', '#FF8C00', '#DC143C', '#6A5ACD', '#00FFFF', '#FF00FF', '#C0C0C0']
