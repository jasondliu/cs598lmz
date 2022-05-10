import weakref
import pygame
import sys
import os.path
import random

from pygame.locals import *

import levels
import events
import colors
import themes
import items

class GameOverException(Exception):
    def __init__(self, state, reason = 'unknown'):
        self.state = state
        self.reason = reason
        Exception.__init__(self, state, reason)

class Character(events.EventHandler):
    """A character."""
    def __init__(self, level, pos=(1,1), time=0, state={}):
        """Create a new character."""
        events.EventHandler.__init__(self)
        self.level = level
        self.pos = list(pos)
        self.time = time
        self.dir = (0,0)
        self.state = state

    def move(self, d, t=None):
        """Move the character by d=(x,y)."""
        if t == None:
            t = self.time
