import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime

from lib.globals import *
from lib.logging import *
from lib.cfg import Config
from lib.logging import log
from lib.db import DB
from lib.notify import Notify
from lib.event import Event
from lib.system import System
from lib.gps import GPS
from lib.sensors import Sensors
from lib.sensors import Sensor
from lib.sensors import SensorList

#
# class Event
#
class Event(object):
    def __init__(self):
        self.id          = None
        self.name        = None
        self.description = None
        self.type        = None
        self.action      = None
        self.active      = None
        self.latitude    = None
        self.longitude   = None
        self.radius      = None
        self.sensor_id   = None
        self.sensor_name = None
        self.sensor_value = None
        self.sensor_value_min = None
        self.sensor_value
