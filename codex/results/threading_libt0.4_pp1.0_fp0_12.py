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
import numpy as np
import os
import argparse

# This is the code for the game

# Some global variables
# The screen
SCREEN_X = 600
SCREEN_Y = 400
# The size of the window
WINDOW_X = 600
WINDOW_Y = 400
# The size of the field
FIELD_X = SCREEN_X
FIELD_Y = SCREEN_Y
# The size of the goal
GOAL_X = 200
GOAL_Y = 20
# The size of the ball
BALL_RADIUS = 10
# The size of the paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
# The speed of the paddle
PADDLE_SPEED = 20
# The size of the block
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
# The size of the wall
