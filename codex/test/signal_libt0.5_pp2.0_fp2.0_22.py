import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import pygame
import random

from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
