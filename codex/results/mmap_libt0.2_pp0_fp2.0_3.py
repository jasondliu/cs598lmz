import mmap
import os
import sys
import time

from pyglet.gl import *
from pyglet.window import key

from . import config
from . import constants
from . import game
from . import graphics
from . import input
from . import menu
from . import sound
from . import util
from . import world

from . import __version__

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.set_minimum_size(800, 600)
        self.set_exclusive_mouse(True)

        self.fps_display = pyglet.clock.ClockDisplay()

        self.world = world.World()
        self.world.load_map(config.get('map'))

        self.game = game.Game(self.world)
        self.game.start()

        self.menu = menu.Menu(self.game)

        self.game.on_game_over.append(self.on_game_
