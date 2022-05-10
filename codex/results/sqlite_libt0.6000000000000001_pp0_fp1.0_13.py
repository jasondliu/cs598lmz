import ctypes
import ctypes.util
import threading
import sqlite3
import re
import os
import sys
import math
import time
import configparser
import json
import urllib.request
import urllib.parse
import logging
from datetime import datetime
from random import randrange
from queue import Queue
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import gui
from . import settings
from . import sound
from . import game
from . import constants
from . import util
from . import entity
from . import player
from . import objects
from . import map
from . import chat

from . import __version__ as VERSION


log = logging.getLogger(__name__)


class GameWindow(gui.Window):
    """Main game window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = configparser.ConfigParser()
        self.config.read(settings.CONFIG_FILE)
        self.settings = settings.Settings(self.config)
