import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# 1 - Import library
import pygame
from pygame.locals import *
import math
import random
import os
import sys
import card
from card import *
from card import Card
from main import *
from player import *
from pool import *
from strings import *
from constants import *
from conffile import Config


def quit():
    import sys
    sys.exit()
    quit()

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
background = pygame.image.load("data/background.png")
card_back_image = pygame.image.load("data/card_back.jpg").convert()
card_back_image = pygame.transform.scale(card_back_image, (CARD_WIDTH, CARD_HEIGHT))
#card_back_image = pygame.transform.scale(card_back_image
