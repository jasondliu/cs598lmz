import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import math
import random
import time

# Showing sensor and motor information 
#   - a sliding window with the current state of the sensors (and motors)
#   - a histogram of the sensor values
#   - a histogram of the motor values

# 1. Parse input
# 2. Initialize screen
# 3. Slide window

#Time to wait between frames
waitTime = 0.1

#Size of the sliding window
windowSize = 100

#Initialize Pygame
pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 16)

#Initialize sensors and motors
sensors = [0 for i
