import weakref
import math
import pygame
import wotsuievents
import wotsui

class ControlIds:
    nan = pygame.USEREVENT


class Control:

    def __init__(self, surface=None, rect=None, pan_area=None,
            borders=True, blend_mode=0, colour=None, colour_disabled=None,
            colour_active=None, colour_inactive=None, colour_borders=None,
            border_width=1, scale_mode=None):
        # surface to draw on (if None, then surface will be parent's surface)
        self.surface = surface
        # Rectangle containing this control (position, dimensions)
        self.rect = rect
        # ID of events to pass to parent
        self.id = ControlIds.nan
        # pointer to parent control
        # access directly using `self.parent()`
        __selfparent = None
        # link to child control and get list of child controls
        # use the methods below and do not access the list directly
        self.child_controls = []
       
