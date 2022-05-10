import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pygame
from pygame.locals import *

import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

class Controller(object):
    def __init__(self):
        pass
        
    def handle_events(self, events):
        pass
        
    def update(self, delta):
        pass

class GLView(object):
    def __init__(self, 
                 title="Python GL View",
                 size = (512, 512), 
                 bpp = 32,
                 fullscreen = False):
        self.size = size
        self.title = title
        self.bpp = bpp
        self.fullscreen = fullscreen
        self.controller = None
        self.running = False
        self.ms_last = 0
        
