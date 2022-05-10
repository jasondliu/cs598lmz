import ctypes
import ctypes.util
import threading
import sqlite3
import time

#
# This code is a modified version of OSSIE's SRI.py
#

class SRI(object):
    def __init__(self, streamID, xstart, xdelta, xunits, subsize, ystart, ydelta, yunits, keywords=[]):
        self.streamID = streamID
        self.xstart = xstart
        self.xdelta = xdelta
        self.xunits = xunits
        self.subsize = subsize
        self.ystart = ystart
        self.ydelta = ydelta
        self.yunits = yunits
        self.keywords = keywords

    def __str__(self):
        return "SRI(streamID=" + self.streamID + ", xstart=" + str(self.xstart) + ", xdelta=" + str(self.xdelta) + ", xunits=" + self.xunits + ", subsize=" + str(self.subsize) + ", ystart=" + str(self.ystart) + ", ydelta=" + str(self.ydelta)
