import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/dev/shm/jelly.db')

import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from planet import Planet
from planet_manager import PlanetManager


window = pyglet.window.Window(1024, 768)
glEnable(GL_DEPTH_TEST)
#glEnable(GL_CULLING)
glCullFace(GL_BACK)
glShadeModel(GL_SMOOTH)
glEnable(GL_BLEND)
glEnable(GL_POINT_SMOOTH)
glEnable(GL_LINE_WIDTH)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(80.0, 1.3333333, 0.1, 1000.0)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

