import types
types.ClassType = types.TypeType = type

import pygame
from pygame.locals import *

import utils
from utils import *

import math
import random

from gameobjects.vector2 import *

class BasicSprite:
	def __init__(self, image, position):
		self.src_image = image
		self.position = Vector2(*position)
		self.speed = 0.
		self.angle = 0.
		
		self.update()
	
	def update(self, time_passed = 0.0):
		self.position += self.direction * self.speed * time_passed
		
		self.image = pygame.transform.rotate(self.src_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

def run():
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Basic
