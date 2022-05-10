import select
import socket
import sys
import threading
import time
import traceback

import pygame

from . import config
from . import constants
from . import controller
from . import display
from . import game
from . import graphics
from . import input
from . import network
from . import sound
from . import ui
from . import util

# TODO:
# - Add a 'quit' button to the pause menu.
# - Add a 'quit' button to the main menu.
# - Add a 'quit' button to the end of game screen.
# - Add a 'quit' button to the options menu.
# - Add a 'quit' button to the credits menu.
# - Add a 'quit' button to the multiplayer menu.
# - Add a 'quit' button to the multiplayer game over screen.
# - Add a 'quit' button to the multiplayer pause menu.
# - Add a 'quit' button to the multiplayer options menu.
# - Add a 'quit' button to the multiplayer host menu.
# - Add a 'quit' button to the multiplayer join menu.
# - Add a 'quit'
