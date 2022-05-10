import mmap
import numpy as np
from scipy import ndimage
import cv2
import time
import os
import datetime
import pygame
from pygame.locals import *
import socket
import sys
import select

# Initialize the pygame modules
pygame.init()
# Initialize the pygame clock
clock = pygame.time.Clock()
# Initialize the pygame font
pygame.font.init()
# Set font size and type
font = pygame.font.SysFont("Arial", 30)
# Set the font color
font_color = (255, 255, 255)

# Set the width and height of the screen
width = 800
height = 600
# Set the screen
screen = pygame.display.set_mode((width, height))
# Set the title on the screen
pygame.display.set_caption("Raspberry Pi Camera")
# Set the background color
background_color = (0, 0, 0)

# Set the camera resolution
camera_width = 640
camera_height = 480

# Set the camera framerate
camera_fram
