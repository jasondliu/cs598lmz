import gc, weakref
import pygame

from . import const
from . import interface
from . import story

import logging
log = logging.getLogger(__name__)

__all__ = [
    "State",
    "StateManager",
    "MenuState",
    "GameState",
    "StoryState",
    "GameOverState",
]

class State(object):
    """State base class"""
    def __init__(self, manager):
        self.manager = manager

    def update(self, dt):
        """Update the state"""
        pass

    def draw(self, surface):
        """Render the state on surface"""
        pass

    def on_key_down(self, key):
        """Called when a key is pressed"""
        pass

    def on_key_up(self, key):
        """Called when a key is released"""
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse is moved"""
        pass

    def on_mouse_button_down(self,
