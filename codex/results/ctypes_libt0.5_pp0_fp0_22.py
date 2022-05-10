import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame
import random
import time
import sys
import os
import math
import numpy as np
from pygame.locals import *
from pygame.color import THECOLORS

from src import utils
from src import consts
from src.consts import *
from src.utils import *
from src.classes import *
from src.buildings import *
from src.pathfinding import *
from src.resources import *
from src.menu import *
from src.map import *
from src.game_functions import *
from src.color_map import *
from src.game_data import *
from src.game_functions import *
from src.game_map import *
from src.game_items import *
from src.game_menu import *
from src.game_messages import *
from src.game_render import *
from src.game_save import *
from src.game_update import *
from src.game_world import *
from src.game_screen import *
from src.game
