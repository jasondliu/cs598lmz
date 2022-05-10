import gc, weakref
import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler
from pyglet.window import mouse
import time
import threading
import math
import random
from euclid import *
import re
import copy

import numpy

# Try to import the Python Imaging Library
try:
    from PIL import Image
    PIL_IMAGE = True
except:
    PIL_IMAGE = False

# Try to import the Numeric Python library
try:
    from numpy import *
    NUMPY = True
except:
    NUMPY = False

# Try to import the Python OpenCV library
try:
    import OpenCV
    OPENCV = True
except:
    OPENCV = False

# Try to import the Python OSC library
try:
    from OSC import *
    OSC = True
except:
    OSC = False

# Try to import the Python Serial library
try:
    import serial
    SERIAL = True
except:
    SERIAL = False

# Try to
