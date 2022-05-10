import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import math

class Ball(object):
    def __init__(self, space, x, y, r):
        self.space = space
        self.r = r
        self.body = pymunk.Body(1, pymunk.inf)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.r)
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
        self.space.add(self.body, self.shape)

    def move_to(self, x, y):
        self.body.position = x, y

    def move_by(self, dx, dy):
        self.body.position = self.body.position + (dx, dy)

