import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

import sys
import os
import time
import threading
import traceback

# SOURCE LINE 9

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import gl

# SOURCE LINE 14

import pymunk
from pymunk import Vec2d
import pymunk.pyglet_util

# SOURCE LINE 18

def flipy(y):
    """Small hack to convert chipmunk physics to pyglet coordinates"""
    return -y+600

# SOURCE LINE 23

def to_pyglet(p):
    new_p = Vec2d(p[0], flipy(p[1]))
    return new_p

# SOURCE LINE 28

def from_pyglet(p):
    new_p = Vec2d(p[0], flipy(p[1]))
    return new_p

# SOURCE LINE 33

class PhysicsObject(object):
    def __
