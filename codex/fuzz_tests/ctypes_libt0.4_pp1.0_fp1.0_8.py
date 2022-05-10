import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import random
import numpy as np
import pygame

from pygame.locals import *
from pygame.color import *

from lib import *

if sys.platform in ['win32','win64']: os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

# Game Settings

WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# Game Objects

class Ball():
    def __init__(self,x,y,w,h,vx,vy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.
