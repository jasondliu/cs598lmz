import gc, weakref

from pygame import display
from pygame.sprite import Group
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE

from .components import Player, EventHandler

class Engine(object):
    """
    Manages the game state and handles input.
    """
    def __init__(self, player, groups, event_handler, screen=None, size=(640, 480)):
        if screen is None:
            screen = display.set_mode(size)
        self.player = player
        self.groups = groups
        self.event_handler = event_handler
        self.screen = screen
        self.size = size
        self.keys = set()
        self.paused = False
        self.clock = pygame.time.Clock()
        self.event_handler.key_down = self.key_down
        self.event_handler.key_up = self.key_up
        self.event_handler.start()

    def key_down(self, key):
        self
