import types
types.ClassType = type

from pygame.locals import *
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

from OpenGL.GLUT import *

from OpenGL.GL.shaders import *

import math
import re
import sys
import time

import numpy

from camera import Camera
import gltext
import shader
import vector

class Viewer:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              HWSURFACE | OPENGL | DOUBLEBUF)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0,
