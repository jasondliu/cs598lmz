import weakref
import logging

from pygame.colordict import THECOLORS, THECOLORS
from pygame import Surface, Color, Rect, Surface, SRCALPHA
from pygame import KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP
from pygame import event, time, draw, font, key
from pygame.locals import QUIT
from pygame.sprite import Sprite

from pacman.colordict import ColorDict
from pacman import constants

# TODO: test
# TODO: better logging
# TODO: better key and event handling
# TODO: fix poor pixel size changing
# TODO: how to handle window resizes?

class BaseLevel(object):
    '''
    Base level class.

    Can be used directly or extended.
    '''
    COLOR_DICT = None
    PIXEL_SIZE = 20

    def __init__(self, show_grid=True):
        self.pixel_size = self.PIXEL_SIZE
        self.show_grid = show_grid
       
