import weakref

# openGL imports
from OpenGL.GL import *
from OpenGL.GLU import *

# pygame imports
import pygame
from pygame.locals import *

# other imports
from math import log10
from ctypes import *
import os,sys

# local imports
import level, editor

# defaults
window_size = (800, 600)
fps = 15

def power_of_two(num):
	"""True if num is a power of two"""
	i = 2
	while i <= num:
		if i == num:
			return True
		i *= 2
	return False


class Texture:
	"""A single OpenGL texture"""
	def __init__(self, index, filename, light=False, mipmap=True, anisotropic=True, max_anisotropy=16):
		# store the filename
		self.filename = os.path.realpath(filename)
		
		# load and convert the image
