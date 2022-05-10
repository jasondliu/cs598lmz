import gc, weakref
from collections import defaultdict, deque
from itertools import chain
from math import sqrt

from pyglet.gl import *
from pyglet.graphics import Batch
from pyglet.window import key

from cocos.director import director
from cocos.euclid import Vector2
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.tiles import RectMapLayer, load

from . import resources
from . import util
from . import view
from . import world

class GameLayer(Layer):
    is_event_handler = True

    def __init__(self, world):
        super(GameLayer, self).__init__()
        self.world = world
        self.world.add_listener(self)
        self.view = view.View(self.world)
        self.view.add_listener(self)
        self.batch = Batch()
        self.add(self.batch)
        self.selected_unit = None
        self.selected_unit_
