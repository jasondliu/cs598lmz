import gc, weakref
import os, sys, re, time, shutil
import logging
import apd.sensors
from optparse import OptionParser
import ConfigParser

# GLOBAL CONFIGURATION CONSTANTS
CONFIG_RAM_CAPACITY = 5*1024*1024
CONFIG_FILE_PATH = '/tmp/config.cfg'
CONFIG_STATE_FILE = '/tmp/config.state'
MEMINFO_CAPACITY = 3
STATUS_INTERVAL = 600
UDP_PORT = 50121
UDP_PORT_STATUS = 50122
CONTROLLER_DOMAIN = "ingenium-system.org"
CONTROLLER_IP = "10.2.0.3"
REMOTE_CONTROLLER = False

# CLASSES
class Validator:
    """ Class to validate text input as python objects """
    
    def __init__(self):
        self.ok = False
        self.object = None
        self.error = None
        
class Config:
    """ Data-only class to hold configuration """
    
    def __init__
