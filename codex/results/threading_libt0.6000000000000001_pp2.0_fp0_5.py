import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math
import numpy as np
import random
import os
import time
import matplotlib.pyplot as plt
import argparse
import copy

def get_data_from_file(filename):
    f = open(filename, 'rb')
    try:
        return pickle.load(f)
    except EOFError:
        return []
    
def save_data_to_file(filename, data):
    f = open(filename, 'wb')
    pickle.dump(data, f)
    f.close()

def init_space(space):
    space.gravity = pymunk.Vec2d(0, -900)
    space.sleep_time_threshold = 0.3
    #space.collision_slop = 0.00001
    #space.add_collision_handler(1, 1).data["handler
