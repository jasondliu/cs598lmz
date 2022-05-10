import select
import sys
import time
import traceback

import pygame
from pygame.locals import *

from . import config
from . import constants
from . import controller
from . import display
from . import game
from . import input
from . import menu
from . import network
from . import sound
from . import util
from . import version

class Main:
    def __init__(self):
        self.config = config.Config()
        self.config.load()
        self.display = display.Display(self.config)
        self.sound = sound.Sound(self.config)
        self.input = input.Input(self.config)
        self.controller = controller.Controller(self.config, self.input)
        self.network = network.Network(self.config, self.controller)
        self.game = game.Game(self.config, self.controller, self.network)
        self.menu = menu.Menu(self.config, self.controller, self.game)
        self.game.menu = self.menu
        self.game.sound = self.
