import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import numpy as np
import time
import math
import random
import copy
import matplotlib.pyplot as plt

# This is the class for the game
class Game:
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.drawing = True
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.space.sleep_time_threshold = 0.3
        self.space.damping = 0.9
        self.space.collision_slop = 0.5
        self.space.add_collision_handler(0, 0).begin = self.collision_begin
