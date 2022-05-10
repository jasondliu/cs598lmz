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
color_palette = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4', '#46f0f0', '#f032e6',
                 '#d2f53c', '#fabebe', '#008080', '#e6beff', '#aa6e28', '#fffac8', '#800000', '#aaffc3', '#808000',
                 '#ffd8b1', '#000080',
