import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n' + '\n'.join(sorted(sys.modules.keys())))).start()
import pygame

# import modules
import pygame
import os
import random
import time
import math
from pygame.locals import *

# import classes
import player
import controller
import enemy
import enemy_controller
import power_up_controller
import power_up
import bullet
import bullet_controller
import collision
import explosion

game = True

# initialize screen
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Space Shooter')

# initialize background
background = pygame.image.load(os.path.join('assets', 'space.png')).convert()
background = pygame.transform.scale(background, (width, height))
screen.blit(background, (0, 0))

# initialize timer
clock = pygame.time.Clock()

# initialize player
player = player.Player
