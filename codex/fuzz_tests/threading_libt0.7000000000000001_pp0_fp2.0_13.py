import threading
threading.stack_size(2**27)
import sys
import pygame
import random as r
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import socket
import pickle
import math
import time
import os
from PIL import Image

'''
    This is the client for a multiplayer pong game.
    The client will connect to the server, then display the game.
    The client will also get user input and send the info back to the server.
'''

PORT = 5555
SIZE = (800,600)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong")

# Used for managing how fast the screen updates
clock = pygame.time.Clock()
