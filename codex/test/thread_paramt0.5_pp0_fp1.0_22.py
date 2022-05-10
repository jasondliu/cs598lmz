import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from pyglet.gl import *
import pyglet

import pymunk
import pymunk.pyglet_util

import math

def draw_circle(pos, rad, color):
    pyglet.graphics.draw(16, pyglet.gl.GL_LINE_LOOP,
        ('v2f', (x for v in [
            (math.cos(t)*rad+pos[0], math.sin(t)*rad+pos[1])
            for t in [math.pi*2*i/16 for i in range(16)]
            ] for x in v))
        , ('c3B', color*16)
        )

