import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import random
import subprocess
import pipes
import json

#import psutil  # psutil is installed with pip

#import pyinotify
#import pynotify

#import gi
#gi.require_version('Notify', '0.7')
#from gi.repository import Notify

#import notify2

#import pync

#import growl

import logging
logging.basicConfig(level=logging.DEBUG)

#logging.basicConfig(level=logging.DEBUG, filename='/tmp/myapp.log')
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

#------------------------------------------------------------------------------

# for debugging
def print_stack():
    import inspect
    print "-"*60
    for frame in inspect.stack():
        print frame[1], frame[2], frame[3]
    print "-"*60

#------------------------------------------------------------------------------

# for debugging
def
