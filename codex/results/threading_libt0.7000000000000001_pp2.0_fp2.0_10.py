import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import numpy as np
from numpy import linalg
from numpy import array
import time
from random import random
from random import randint
from random import uniform
from math import sin
from math import cos

# =========================
# ====== TRAINING =========
# =========================

# =========================
# ====== CONSTANTS =========
# =========================

x_screen_size = 1000
y_screen_size = 1000

# window size
width = 800 
height = 400

# agent's body (no tail)
body_length = 20
body_height = 15

# agent's tail
tail_length = 25
tail_width = 5

# distance between the agent's body and the tip of the tail
distance_between_agent = body_height/2 + tail_width

# agent's initial position
agent_initial_position = (x_screen_size/2, y_screen_
