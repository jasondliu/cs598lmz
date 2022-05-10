import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import pygame
from pygame.locals import *

import thread

class PApplet(object):
    # Some constants
    LEFT = 1
    RIGHT = 2
    CENTER = 3
    TOP = 101
    BOTTOM = 102
    BASELINE = 103
    RADIUS = 0
    CORNER = 1
    CORNERS = 2
    CENTER_RADIUS = 3
    CENTER_DIAMETER = 3
    OPEN = 1
    CLOSE = 2
    CHORD = 0
    PIE = 1
    PROJECT = 0
    SQUARE = 1
    ROUND = 2
    BEVEL = 3
    MITER = 4
    RGB = 1
    ARGB = 2
    HSB = 3
    ALPHA = 4
    CMYK = 5
    TIFF = 0
    TARGA = 1
    JPEG = 2
    GIF = 3
    BLUR = 11
    GRAY = 12
    INVERT = 13
    OPAQUE = 14
    POSTERIZE = 15
    THRES
