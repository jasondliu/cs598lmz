import weakref

import pygame

from . import scene
from . import settings

import logging
_log = logging.getLogger(__name__)


class SceneManager(object):
    def __init__(self):
        _log.info("Scene manager initialising")
        self._display_size = settings.display_size
        self._running = False
        self.screen = None
        self.scene = None

    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    def init(self):
        _log.info("Initialising")
        pygame.display.init()
        pygame.font.init()
        self._running = True
        self.screen = pygame.display.set_mode(self._display_size)
        self.clock = pygame.time.Clock()

    def start(self):
        _log.info("Starting")
