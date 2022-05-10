import threading
threading.stack_size(2**27)
import sys
import math
import pygame
from pygame.locals import *
import pygame.gfxdraw
import random
import copy
import time
import os

# Game settings

# State of the game
# 0 = not started
# 1 = started
# 2 = finished
state = 0

# List of players
players = []

# List of blocks
blocks = []

# List of items
items = []

# List of bullets
bullets = []

# List of explosions
explosions = []

# List of dead players
dead = []

# List of dead bullets
dead_bullets = []

# List of dead items
dead_items = []

# List of dead explosions
dead_explosions = []

# List of dead blocks
dead_blocks = []

# List of dead enemies
dead_enemies = []

# List of enemies
enemies = []

# List of enemy bullets
enemy_bullets = []

# List of dead enemy bullets
dead_enemy_bullets = []
