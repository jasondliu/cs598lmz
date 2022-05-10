import weakref

import pygame

from . import constants as c
from . import control
from . import setup
from . import tools


class Game:
    """
    This class handles all the main functionality
    of the game.
    """
    def __init__(self):
        """
        Get the game ready to play.
        """
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.keys = pygame.key.get_pressed()
        self.done = False
        self.current_time = 0.0
        self.level_rect = pygame.Rect((0, 0), c.LEVEL_SIZE)
        self.level = setup.LEVEL1
        self.level_surface = setup.get_level_surface(self.level)
        self.viewport = setup.make_viewport(self.screen_rect,
                                            c.LEVEL_SIZE)

        # Create sprite
