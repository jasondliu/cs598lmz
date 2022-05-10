import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import numpy as np
import time
import math
import os
import random
import pickle
import datetime
import copy
import matplotlib.pyplot as plt
import cv2
from scipy.interpolate import interp1d
from scipy.interpolate import spline

# Importing the DQN
from DQN_final import DQN

# Importing the other Python files
from parameters import *
from transitionTable import *
from game_state import GameState
from ball import Ball
from block import Block
from utility import *
from plotting import *
from collections import deque

# Creating the display surface
display_surface = pygame.display.set_mode((WINSIZE,WINSIZE))

# Initializing PyGame
pygame.init()
pygame.display.set_caption("Breakout")
clock = pygame.time
