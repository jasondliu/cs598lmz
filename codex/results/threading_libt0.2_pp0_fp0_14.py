import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import math
import random
import numpy as np
import time
import os
import pickle

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((1000, 700))

# Turn off alpha since we don't use it.
screen.set_alpha(None)

# Enable this to make the simulation run faster
# Turn off alpha since we don't use it.
screen.set_alpha(None)

# Show the "mouse pointer"
pygame.mouse.set_visible(True)

# Hide the "mouse pointer"
#pygame.mouse.set_visible(False)

# This can be helpful for debugging
# It shows a lot of stuff in the console
#debug = True
debug = False

# Create a world for physics
world = pymunk.Space()
world.gravity
