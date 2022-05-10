import weakref

import pygame

import pymunk

from . import settings
from . import util
from . import physics
from . import graphics
from . import sound
from . import events

class Game(object):
    """
    The game object.
    """
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.events = events.Events()
        self.entities = []
        self.entity_ids = {}
        self.entity_groups = {}
        self.entity_group_ids = {}
        self.entity_group_id_counter = 0
        self.entity_group_id_counter_lock = Lock()
        self.entity_group_ids_lock = Lock()
        self.entity_groups_lock = Lock()
        self.entity_ids_lock = Lock()
        self.entities_lock = Lock()
        self.game_state = None
        self.game_
