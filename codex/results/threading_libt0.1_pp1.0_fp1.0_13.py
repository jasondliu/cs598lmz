import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import os
import pickle
import neat
import visualize
import multiprocessing
import glob
import winsound

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((600, 600))

# Run until the user asks to quit
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize PyMunk
space = pymunk.Space()
space.gravity = (0.0, -900.0)

# Create the car
mass = 1
radius = 14
inertia = pymunk.moment_for_circle(mass, 0
