import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from time import sleep
from random import random
from math import sin, cos, pi

from pyglet.gl import *
from pyglet.window import key

from shaders import *
from scene import *
from camera import *
from light import *
from material import *
from mesh import *
from texture import *
from util import *

window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    scene.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

scene = Scene()

camera = PerspectiveCamera()
