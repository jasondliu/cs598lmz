import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import logging
import threading
import traceback

import pyglet
from pyglet.gl import *
from pyglet.window import key

from pymunk import Vec2d
import pymunk
import pymunk.pyglet_util

logger = logging.getLogger(__name__)

# SOURCE LINE 21

class Game(object):
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.space.sleep_time_threshold = 0.3
        self.space.collision_slop = 0.5
        self.space.iterations = 10
        self.space.damping = 0.9
        self.space.add_collisionpair_func(0, 0, self.collision_handler, None)
        self.space.add_collisionpair_func(0, 1, self.
