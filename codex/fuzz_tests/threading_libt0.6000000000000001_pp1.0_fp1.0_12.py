import threading
threading.stack_size(2**27)
import sys
import pyglet
from pyglet.window import key
from pyglet.gl import *

import numpy as np
import Box2D
from Box2D.b2 import (edgeShape, circleShape, fixtureDef, polygonShape, revoluteJointDef, contactListener)

# Own imports
import car
import road
import constants
import utils

# Initialize world
world = Box2D.b2World(gravity=(0, 0), doSleep=True)

# Initialize road
road = road.Road(world)

# Initialize cars
cars = []
for _ in range(constants.N_CARS):
    car = car.Car(world, road)
    cars.append(car)

# Initialize pygame
pyglet.options['audio'] = ('directsound', 'openal', 'pulse', 'silent')
window = pyglet.window.Window(width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT, vsync=False
