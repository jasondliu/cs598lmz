import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import random
import math

# Showing sensor and restarting settings
draw_sensors = False
restart = True

# Physics collision types
COLLTYPE_DEFAULT = 0
COLLTYPE_MOB = 1
COLLTYPE_WALL = 2

# Physics shapes
MOB_SIZE = 30
MOB_ELASTICITY = 0.95
WALL_ELASTICITY = 0.95

# Physics forces
MOB_FRICTION = 0.9
MOB_MASS = 10
MOB_FORCE = 10000

# Physics sensor
SENSOR_SIZE = 10
SENSOR_ELASTICITY = 0.95
SENSOR_FRICTION = 0.9
SENSOR_MASS = 1

# Screen
SCREEN_X = 600
SCREEN_Y = 400

# Orientation
orientation = 0

# Actions
# 0 - forward
