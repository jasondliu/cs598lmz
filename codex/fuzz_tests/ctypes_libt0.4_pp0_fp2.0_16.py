import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import numpy as np
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

# PyGame init
width = 1000
height = 700
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Turn off alpha since we don't use it.
screen.set_alpha(None)

# Showing sensors and redrawing slows things down.
show_sensors = True
draw_screen = True


class GameState:
    def __init__(self):
        # Global-ish.
        self.crashed = False

        # Physics stuff.
        self.space = pymunk.Space()
        self.space.gravity = pymunk.Vec2d(0., 0.)

        # Create the car.
        self.create_car
