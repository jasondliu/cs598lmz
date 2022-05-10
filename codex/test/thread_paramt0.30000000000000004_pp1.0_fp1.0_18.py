import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import the interface
import pygame
import math
import random
import time
import numpy as np

# Import the agent
from agent import Agent

# Import the environment
from environment import Environment

# Import the world
from world import World

# Import the utils
from utils import *

# Import the constants
from constants import *

# Import the pygame constants
from pygame.locals import *

# Import the pygame constants
from pygame.locals import *

# Initialize the pygame
pygame.init()

# Initialize the font
pygame.font.init()

# Initialize the clock
clock = pygame.time.Clock()

# Create the window
window = pygame.display.set_mode(WINDOW_SIZE)

# Set the window title
pygame.display.set_caption(WINDOW_TITLE)

# Create the environment
environment = Environment()

# Create the world
