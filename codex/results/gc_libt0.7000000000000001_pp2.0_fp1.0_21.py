import gc, weakref

import pygame
import pygame.mixer
import pygame.fastevent
import pygame.sprite
import pygame.time
import pygame.draw
import pygame.image
import pygame.font
import pygame.mouse
import pygame.event
import pygame.locals
import pygame.display

import ui
import ui.widgets
import ui.layout
import ui.layout.containers
import ui.layout.columns
import ui.layout.rows
import ui.layout.grids
import ui.layout.panels
import ui.layout.scrollers
import ui.layout.border

from utils.event import *

class Window(ui.layout.containers.Container):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.padding = 0
        self.margin = 0

        self.layout = ui.layout.panels.Panel([ui.layout.border.Border, ui.layout.
