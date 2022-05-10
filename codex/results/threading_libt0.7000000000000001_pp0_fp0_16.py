import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import random
from operator import attrgetter
import json
import numpy as np
from . import physics_utils

def init(width, height):

    ### Pygame init
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    ### Disable alpha since we don't use it.
    screen.set_alpha(None)

    ### Turn off mouse visibility
    pygame.mouse.set_visible(False)

    ### Init space
    space = pymunk.Space()
    space.gravity = pymunk.Vec2d(0.,0.)

    ### Add static line
    static_body = space.static_body
    static_lines = [pymunk.Segment(static_body, (0.0, 1.0), (0.0, height), 0.0),
