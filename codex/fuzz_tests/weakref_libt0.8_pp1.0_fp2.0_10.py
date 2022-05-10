import weakref

import pygame
from pygame import locals as const
from pygame import draw
from ..core import event

from .control import Control
from .widget import Widget
from .. import font
from .. import layout
from .. import text
from .. import decorators
from .. import util

from ..widgets import selectbuttons


@decorators.memoize
def memoized_image(filename):
    return pygame.image.load(filename).convert_alpha()

class ActionWidget(Widget):
    u""" This will be used for the top area widgets. Do not use this
    for anything that will actually be used.
    """
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.control_area = None
        self.action_area = None
        self.action_area_width = 0
        self.control_area_width = 0
        self.border_size = self.theme.get('ActionWidget', 'border_size')
        self.padding = 0
       
