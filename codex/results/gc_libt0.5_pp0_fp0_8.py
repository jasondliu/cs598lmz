import gc, weakref
import threading

import pygame

from pygame.locals import *

import display, configuration, game
from common import *

class Game(object):
    def __init__(self):
        pygame.init()

        self._running = True
        self._paused = False
        self._quit = False

        self._clock = pygame.time.Clock()

        self._config = configuration.Configuration()
        self._display = display.Display(self._config)
        self._game = game.Game(self._display)

    def run(self):
        self._display.start()

        self._game.start()

        while self._running:
            self._clock.tick(60)

            self._display.process_events()
            self._game.process_events()

            if not self._paused:
                self._display.update()
                self._game.update()
                self._display.render()

            if self._quit:
                self._running = False

        self._game.stop()
        self._display.stop()

        pygame
