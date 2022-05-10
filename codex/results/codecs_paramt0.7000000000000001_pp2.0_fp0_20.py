import codecs
codecs.register_error('strict', codecs.ignore_errors)

import logging
logger = logging.getLogger('pylife')

import random

import pygame
import freetype
import sqlite3

from pygame.locals import *

import pylife.common.conf as conf

from pylife.common.components import GameComponent, GameObject, GameButton, GameText, GameCheckBox, GameRadioButton, GameLabel, GameTextInput
from pylife.common.resources import ResourceManager, Color, FontManager

class GameApp:
    def __init__(self, name, icon, conf):
        pygame.init()
        pygame.display.set_caption(name)

        self.name = name
        self.icon = icon
        self.conf = conf

        self.screen = pygame.display.set_mode((self.conf.screen_width, self.conf.screen_height), self.conf.screen_flags)

        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self
