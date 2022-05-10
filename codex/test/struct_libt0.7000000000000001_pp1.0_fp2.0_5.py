import _struct
import cv2
import os
import numpy as np
import pygame
from pygame.locals import *
import sys

# This is a simple object class that will be used to store the
# color data of each pixel on the screen.
class RGB:
    r = 0
    g = 0
    b = 0

# This function will set the point (x, y) to the color RGB
def setPixel(x, y, color):
    screen.set_at((x, y), color)

# This function will return a pixel at the given (x, y) location
def getPixel(x, y):
    return screen.get_at((x, y))

# This function will draw a line from (x1, y1) to (x2, y2)
# This is a naive implementation that just uses a "brute-force"
# method to draw the line - we simply iterate along the length
# of the line and set each pixel individually.
