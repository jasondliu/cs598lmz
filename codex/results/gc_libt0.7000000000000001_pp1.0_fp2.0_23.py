import gc, weakref

import pygame
from pygame.locals import *

import random

try:
    import psyco
    psyco.full()
except ImportError:
    pass

class Object:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dead = False
        
    def get_rect(self):
        return Rect(self.x, self.y, self.w, self.h)
        
    def update(self, map, objects):
        pass
    
    def draw(self, surface):
        pass
    
    def destroy(self):
        self.dead = True
        
class Player(Object):
    def __init__(self, x, y, w, h):
        Object.__init__(self, x, y, w, h)
        
        self.health = 100
        
    def update(self, map, objects):
        pass
    
    def draw(self, surface
