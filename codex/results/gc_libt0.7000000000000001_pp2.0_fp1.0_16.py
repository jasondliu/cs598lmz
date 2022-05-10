import gc, weakref
import logging
from types import FunctionType

import pygame

import serge.actor
import serge.common
import serge.events
import serge.render
import serge.sound
import serge.zone
import serge.world

from serge.common import Serializable
from serge.render import Camera, IRenderable, RenderItem
from serge.sound import Engine as SoundEngine
from serge.zone import ActiveZone
from serge.world import World as BaseWorld

from theme import G, theme

log = logging.getLogger('serge.engine')


class Engine(object):
    """The main engine for the game"""
    
    def __init__(self, options):
        """Initialise the engine"""
        self.options = options
        self.screen = serge.render.Screen(theme.DEFAULT_SCREEN_SIZE, theme.DEFAULT_SCREEN_MODE, theme.DEFAULT_SCREEN_FLAGS)
        self.input_manager = serge.events.getInputManager()
        self.input_manager.setEngine
