import gc, weakref

#import logging
#logging.basicConfig(level=logging.DEBUG)

import pyglet
from pyglet.gl import *
from pyglet.window import key

import numpy as np

from util import *
from obj import *

from pyglet.window import key
from pyglet.window import mouse

from pyglet.gl import *

class Scene(object):
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def draw(self):
        for o in self.objects:
            o.draw()

class SceneViewer(object):
    def __init__(self, scene):
        self.scene = scene

        self.window = pyglet.window.Window(width=1024, height=768,
                                           caption='SceneViewer')
        self.window.set_exclusive_mouse(True)
        self.
