import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import pickle
from collections import deque
import cv2
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from keras.optimizers import Adam
from keras.models import load_model
from keras import backend as K
from keras.utils import plot_model

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

# Showing sensors or not
show_sensors = True

# Global variables
# ----------------

# Images
path = os.getcwd()
path = path
