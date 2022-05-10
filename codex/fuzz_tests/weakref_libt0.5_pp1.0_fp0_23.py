import weakref

import pygame

from . import resources
from . import settings
from . import scene
from . import scene_manager


class Game(object):

    def __init__(self, width, height, title, version, fps=settings.FPS):
        self.width = width
        self.height = height
        self.title = title
        self.version = version
        self.fps = fps
        self.running = False
        self.screen = None
        self.clock = None
        self.scene_manager = None
        self.scenes = {}
        self.events = {}
        self.keys = {}
        self.__register_default_events()

    def __register_default_events(self):
        self.register_event(pygame.QUIT, self.quit)
        self.register_event(pygame.KEYDOWN, self.handle_keydown)
        self.register_event(pygame.KEYUP, self.handle_keyup)

    def register_event(self, event_type, handler):
        self.events[event_type] = handler
