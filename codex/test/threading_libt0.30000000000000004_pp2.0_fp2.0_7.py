import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import math
import random
import numpy as np
import time
import os

# Importing the DQN
from DQN import DQN

# Creating the environment
class GameInstance:
    def __init__(self):
        # Initialize game and create screen object
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Pymunk Test")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Arial", 16)
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.draw_options.flags = self.draw
