import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

import random

import math

from PIL import Image



def loadTexture(filename, texture_id):
	surface = pygame.image.load(filename)
	image = pygame.image.tostring(surface, "RGBA", 1)

	width = surface.get_width()
	height = surface.get_height()

	glBindTexture(GL_TEXTURE_2D, texture_id)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

def loadCubeMap(filename, texture
