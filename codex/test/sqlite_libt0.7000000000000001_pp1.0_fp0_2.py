import ctypes
import ctypes.util
import threading
import sqlite3

from datetime import datetime

import config as cfg
import sqlite_utils as sqlite
import gui_utils as gui
import logging
import log
import service

#-------------------------------------------------------------------------------
class DHT11Sensor(service.Sensor):
    #---------------------------------------------------------------------------
    def __init__(self, serviceName, device, debugLevel):
        service.Sensor.__init__(self, serviceName, device, debugLevel)
        self.logTag = serviceName
        self.thread = None
        self.threadRun = False

        self.dht11_lib = None
        self.dht11_lib_path = None

        self.dht11_lib_path = ctypes.util.find_library('dht11')
        if self.dht11_lib_path is not None:
            self.dht11_lib = ctypes.cdll[self.dht11_lib_path]
                #set_debug(ctypes.c_int(debugLevel))
