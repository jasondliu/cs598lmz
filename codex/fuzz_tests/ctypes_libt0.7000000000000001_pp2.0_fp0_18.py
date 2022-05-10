import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import os
import sys
import pygame
import math
from pygame.locals import *
from random import randint

pygame.init()

size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 20)
font_big = pygame.font.Font(None, 50)

# Game states
START = 0
PLAYING = 1
GAMEOVER = 2
PAUSE = 3

# Game state
game_state = START

# Snake
snake_pos = [400, 300]
snake_body = [[400, 300], [400, 320]]

