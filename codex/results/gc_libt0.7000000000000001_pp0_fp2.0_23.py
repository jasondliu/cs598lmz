import gc, weakref

from pyglet import gl, image
from pyglet.graphics import Batch, StateGroup, TextureGroup
from pyglet.image import Texture
from pyglet.window import key

from noise import pnoise2, snoise2

from . import camera, entities, player, terrain, util
from .constants import *
from .window import Window

__all__ = [
    'World'
]

class World(object):
    """Game world"""

    def __init__(self, window=None):
        self.window = window
        if window is None:
            self.window = Window()
        self.window.push_handlers(self)

        self.batch = Batch()

        self.texture_group = TextureGroup(self.window.textures['terrain'])

        self.perlin1 = Perlin(self)
        self.perlin2 = Perlin(self)
        self.perlin3 = Perlin(self)
        self.perlin4 = Perlin(self)
        self.perlin5 = Perlin(self
