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
import time
import os
import cv2

# PyGame init
width = 1000
height = 700
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Showing sensors
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Global varaibles
space = pymunk.Space()
space.gravity = pymunk.Vec2d(0., 0.)
cars = []

# Creating walls
static = [
    pymunk.Segment(
        space.static_body,
        (0, 1), (0, height), 1),
    pymunk.Segment(
        space.static_body,
        (1, height), (width, height), 1),
    p
