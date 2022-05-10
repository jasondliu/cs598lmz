import gc, weakref, sys
import pygame as pg
import os
from .. import tools, prepare
from ..components.animation import Animation
from ..components.labels import Blinker


class Menu(tools._State, object):
    """Menu state class."""
    def __init__(self, screen_rect):
        """Menu state init method."""
        super(Menu, self).__init__()
        self.next = "BRIEFING"
        self.screen_rect = screen_rect
        self.title = Blinker("ROCKY", {"midtop": self.screen_rect.center},
                                  prepare.FONTS["Saniretro"], 200, (255, 255, 255))
        self.title.animate(1)
        self.base_image = prepare.GFX["menu-background"]
        self.base_image_rect = self.base_image.get_rect(center=self.screen_rect.center)
        self.key_image = prepare.GFX["keyboard"]
        self.key_rect = self.key_image.get_rect()
       
