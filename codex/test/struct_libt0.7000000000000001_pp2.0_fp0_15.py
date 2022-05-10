import _struct
import weakref

# pyglet
import pyglet
from pyglet.gl import *

# pymunk
import pymunk

# cocos2d
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.text import Label

# my code
import collision
import bullet
import enemy
import enemy_bullet
import ui


class Game(Layer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()

        self.batch = pyglet.graphics.Batch()
        self.sprites = weakref.WeakKeyDictionary()

        self.label = Label('Score: 0', font_size=8,
                           x=10, y=10,
                           anchor_x='left', anchor_y='top',
                           color=(255, 255, 255, 255),
                           batch=self.batch)

        self.score = 0

        self._create_world()

    def _create_world(self):
        self.space
