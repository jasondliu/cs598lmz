import gc, weakref
from math import sin, cos, pi, sqrt, hypot
from random import randrange, randint, choice, random, gauss
from functools import partial
from time import time
from pyglet import image, gl
from pyglet.window import Window, key
from pyglet.window.event import EventDispatcher
from pyglet.sprite import Sprite
from pyglet.clock import schedule
from pyglet.graphics import *
from pyglet.window import mouse as mouse_module
from pyglet.window import key as key_module
import pyglet.window
from pyglet.app import run


class Game(EventDispatcher):
    def __init__(self, **kwargs):
        super(Game, self).__init__()
        self.batch = Batch()
        self.window = window = Window(**kwargs)
        window.push_handlers(self)

        # This is a sprite group that renders quickly
        self.static_sprites = sprite.Group()

        # This is a sprite group for everything else
        self.
