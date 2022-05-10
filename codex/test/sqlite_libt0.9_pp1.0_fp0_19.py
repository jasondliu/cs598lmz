import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import sys

from optparse import OptionParser
from gps import *
from time import *

b_verboseP = True

gpsd_i = None



class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        global gpsd_i

        # Bring up the gpsd service by calling gpsd library
        gpsd = ctypes.CDLL(ctypes.util.find_library("gps"))
        # Starting the stream information to port 2947
        gpsd_i = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True

    def run(self):
        global gpsd_i
        global gpsd
        gpsd.gps_stream(gpsd_i, WATCH_ENABLE)
