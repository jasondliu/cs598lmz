import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import pymunk
from pymunk import Vec2d
import random
import math
import time

# Showing sensors and redrawing slows things down, turns off by default.
show_sensors = True
draw_screen = True

class GameState:
    def __init__(self):
        # Global-ish.
        self.crashed = False

    def frame_step(self, action):
        if action == 0:  # Turn left.
            self.car.steer += -1
        elif action == 1:  # Turn right.
            self.car.steer += 1
        elif action == 2:  # Accelerate.
            self.car.motor = 1.0
        elif action == 3:  # Reverse.
            self.car.motor = -0.5
        elif action == 4:  # Brake.
            self.car.brake = 0.8


