import _struct
from collections import defaultdict
from itertools import chain
from random import random

from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

from . import constants
from . import utils
from . import vector


class Entity(Sprite):
    """Base class for all game entities.

    This class inherits from pygame.sprite.Sprite and provides basic
    functionality for all entities.
    """

    def __init__(self, game, *groups):
        """Initialize the entity."""
        super().__init__(*groups)
        self.game = game
        self.name = "Entity"
        self.layer = 0
        self.image = None
        self.rect = None
        self.mask = None
        self.pos = None
        self.vel = vector.Vector()
        self.acc = vector.Vector()
        self.friction = 0.0
        self.gravity = 0.0
        self.max_vel = 2.0
        self.collision_rect = None
