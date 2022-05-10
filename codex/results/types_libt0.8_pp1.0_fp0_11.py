import types
types.ModuleType.__repr__ = lambda self: self.__name__
 
from __future__ import division

from itertools import count
import math
import random

import pyglet
from pyglet.window import key
from pyglet.window import mouse

from vector2d import Vector2D

game_window = pyglet.window.Window(caption = "Asteroids",
                                   width = 800,
                                   height = 600)

game_engine = pyglet.media.Player()
game_engine.queue(pyglet.resource.media("Resources/sound/engine.wav"))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Global Metadata
#

"""

This variable is used to store the resources for our game.

"""
resources = {}

"""

This variable is used to store the list of sprites that we have currently in
game.

"""
sprites = []

