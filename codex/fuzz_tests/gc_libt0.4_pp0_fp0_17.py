import gc, weakref
from types import MethodType

from pygame import Surface, Rect
from pygame.sprite import Sprite
from pygame.locals import *

from util import *
from base import *
from core import *
from events import *
from widgets import *
from layout import *
from graphics import *
from menu import *

from pygame.font import SysFont

class Text(Widget):
    """
    A simple text label widget.
    """
    def __init__(self, text="", font=None, color=(255, 255, 255), bgcolor=None,
                 padding=0, align=0, valign=0, **params):
        Widget.__init__(self, **params)
        self.text = text
        self.font = font or SysFont("default", 12)
        self.color = color
        self.bgcolor = bgcolor
        self.padding = padding
        self.align = align
        self.valign = valign
        self.update()

    def update(self):
        self.image = self.font.render
