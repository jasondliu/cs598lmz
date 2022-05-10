import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import pygame
import random
import math
import time
from pygame.locals import *

#pygame.init()

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0))

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.display.set_caption('Fractal')

#screen.fill((0, 0, 0))

#pygame.display.flip()

#time.sleep(5)

#sys.exit()

#screen = pygame.display.set_mode((0, 0))

#screen = pygame.display.set_mode((width, height))

#screen.fill((0, 0, 0))

#pygame.display.flip()

#time.sleep(5)

#sys.exit()

#screen = pygame
