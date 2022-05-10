import ctypes
import ctypes.util
import threading
import sqlite3
import re

from pyglet.gl import *
from pyglet import window
from pyglet import clock
from pyglet import image
from pyglet import font
from pyglet import text
from pyglet import event

#from util import *

from rpc import *
from mote import *
from sensor import *
from ui import *
from net import *
from node import *
from world import *

from app import *
from app_node import *
from app_sensor import *
from app_console import *
from app_rpc import *
from app_net import *
from app_mote import *

class WorldView(object):
    def __init__(self, world, rpc, mote, sensor, net):
        self.world = world
        self.rpc = rpc
        self.mote = mote
        self.sensor = sensor
        self.net = net
        self.apps = []
        self.apps.append(AppMote(self))
        self.apps.append(AppSensor(self))
