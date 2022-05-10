import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import time
import random
import math

#Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Define the screen size
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

#Define the size of the paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

#Define the size of the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#Define the speed of the paddle and ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#Define the score
score = 0

#Define the number of lives
lives = 3

