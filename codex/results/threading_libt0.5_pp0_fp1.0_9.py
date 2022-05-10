import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import pymunk
from pymunk import Vec2d
import math
import random
import datetime
import time
import pickle
import os
import numpy as np
import cv2
import tensorflow as tf
import time

# Game options/settings
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

# Global vars
SCREENWIDTH  = 288
SCREENHEIGHT = 512

# Images
IMAGES = {}
IMAGES['numbers'] = (
    pygame.image.load('images/0.png').convert_alpha(),
    pygame.image.load('images/1.png').convert_alpha(),
    pygame.image.load('images/2.png').convert_alpha(),
    pygame.image.load('images/3.png').convert_alpha(),
    pygame.image.load('images/4.
