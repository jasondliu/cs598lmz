import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import time
import numpy as np
import math
import random
import os

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

# Physics stuff.
space = pymunk.Space()
space.gravity = pymunk.Vec2d(0., 0.)

# Create the car.
inertia = pymunk.moment_for_circle(1, 0, 14, (0, 0))
body = pymunk.Body(1, inertia)
body.position = 50, height - 100
car
