import threading
threading.stack_size(67108864)

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

import numpy as np
from numpy.linalg import inv
import math

import time
import sys

# Importing the DQN
from a2c_agent import DQN

# Initialize the game engine
pygame.init()

class ArmEnv(object):
    def __init__(self, arm_info):
        # General info
        self.arm_info = arm_info
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.arm_info['upper_arm_length'] = 100
        self.arm_info['forearm_length'] = 136
        self.arm_info
