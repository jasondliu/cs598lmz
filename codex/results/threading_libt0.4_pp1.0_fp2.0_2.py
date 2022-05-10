import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import random
import time
import math
import os
import numpy as np
from collections import deque
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0

# Set the width and height of the screen [width, height
