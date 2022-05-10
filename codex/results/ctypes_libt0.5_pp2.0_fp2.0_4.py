import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import numpy as np
import pygame
from pygame.locals import *
from random import randint

import time

from PIL import Image

import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((1000, 1000))

# Run until the user asks to quit
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the title of the window
pygame.display.set_caption('A*')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the grid
grid_size = 20
grid_width = 1000
grid_height = 1000

# Set up the start and end points
start_x = 0
start_y = 0
end_
