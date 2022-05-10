import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import math
import random
import time
import os
import copy
import pickle

# Game Initialization
pygame.init()
pygame.font.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Global Variables
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Resources
pipe_image = pygame.image.load(os.path.join("images","pipe.png"))
background_image = pygame.image.load(os.path.join("images","background.png"))

# Bird Class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super(Bird, self).__init__()
