import weakref
from collections import deque
from math import cos, sin, radians, hypot, pi
import random

from pygame.locals import *
from pygame import Rect, Surface
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import LayeredUpdates
from pygame.sprite import collide_circle

from game_modules.constants import *
from game_modules.settings import *
from game_modules.utilities import *
from game_modules.level_manager import *
from game_modules.game_manager import *
from game_modules.player import *
from game_modules.hud import *
from game_modules.enemies import *
from game_modules.projectiles import *
from game_modules.powerups import *
from game_modules.bonuses import *
from game_modules.explosion import *
from game_modules.ship_explosion import *
from game_modules.transition import *

class Game(object):
    def __init__(self):
        self.init_pygame()
        self.init
