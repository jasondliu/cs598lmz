import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import numpy as np
import random
import math
import time
import os
import datetime
import pickle
import matplotlib.pyplot as plt

# pygame.init()

# This is the main class of the game.
# It is responsible for the game loop, drawing, and physics
class Game:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        self.running = True
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.space.damping = 0.9
        self.space.sleep_time_threshold = 0.2
        self.space.idle_speed_threshold = 0.1
        self.space.collision_sl
