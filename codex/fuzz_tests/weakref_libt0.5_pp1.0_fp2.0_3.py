import weakref

from pygame import Rect, Surface
from pygame.locals import *

from pygameui.widgets.base import Widget
from pygameui.locals import *


class ScrollArea(Widget):
    def __init__(self, rect, bg_color=(0, 0, 0), parent=None):
        Widget.__init__(self, rect, bg_color, parent)
        self.child = None
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_width = 0
        self.scroll_height = 0
        self.scroll_view_height = 0
        self.scroll_view_width = 0
        self.scroll_bar_width = 0
        self.scroll_bar_height = 0
        self.scroll_bar_x = 0
        self.scroll_bar_y = 0
        self.scroll_view_x = 0
        self.scroll_view_y = 0
        self.scroll_bar_visible = False
        self.scroll_view_visible = False
        self.scroll_
