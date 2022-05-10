import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import os
import glob

try:
    from coreaudio import *
except ImportError:
    pass
    

logging.basicConfig(level=logging.DEBUG)

DeviceManagerEmu = None
try:
    from enigma import DeviceManager
    DeviceManagerEmu = DeviceManager()
    import config
    DeviceManagerEmu.registerProvider(config.Init)
except ImportError:
    pass
    

from twisted.internet import reactor
from twisted.python import log
log.startLogging(sys.stdout)
from Net import Server
from Net import create_twisted_endpoint
from enigma import Enigma
from Scripting import Scripting # Scripting engine


config_version = 1

#import iface
#winsock_available = iface.winsock_available()

class Config:
    def __init__(self):
        global config_version
        self.version = config_version
    
