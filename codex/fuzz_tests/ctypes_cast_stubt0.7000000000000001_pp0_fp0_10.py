import ctypes
ctypes.cast(0, ctypes.py_object)

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pyglet.gl import *
from pyglet.gl.glu import *
from pyglet import image

import pyglet

from shader import Shader
from model import Model

from math import sin, cos

class Camera(object):
    def __init__(self):
        self.pos = [0.0, 0.0, 0.0]
        self.rot = [0.0, 0.0, 0.0]
        
    def update(self, dt, key):
        s = dt*10.0
        
        if key[key.W]: self.pos[0] += s*sin(self.rot[1])
        if key[key.S]: self.pos[0] -= s*sin(self.rot[1])
        if key[key.A]: self.pos[1] -= s*cos(self.rot[1])
