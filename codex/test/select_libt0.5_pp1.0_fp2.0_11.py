import select
import socket
import sys
import time

import pygame

from pygame.locals import *

# Settings

# Screen size
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 150

# Ball settings
BALL_WIDTH = 20
BALL_HEIGHT = 20

# Game settings
FPS = 60

# Classes
class Ball:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.dir_x = -1
        self.dir_y = -1
        self.speed = 10

