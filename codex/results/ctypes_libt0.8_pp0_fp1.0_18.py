import ctypes
ctypes.CDLL('./lib/x86_64-linux-gnu/libGL.so')

import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')

import math
import numpy as np
import matplotlib.pyplot as plt

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

from module import bresenham_circle, getEllipse, getCircle
from module.plane import Plane
from module.config import (
    WINDOW_HEIGHT, WINDOW_WIDTH,
    WINDOW_POSITION_X, WINDOW_POSITION_Y,
    BG_COLOR, LINE_COLOR
)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self):
        center_z = 1
        circle = getCircle(self.center[1], self.center[0], self.radius)
        glBegin
