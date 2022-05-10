import ctypes
import ctypes.util
import threading
import sqlite3

from sys import platform
from math import floor
from types import MethodType

# Here we will be parsing command line arguments.
from optparse import OptionParser


# Imports for outputing progressbar.
from progressbar import ProgressBar, Percentage, Bar, ETA, \
                        FileTransferSpeed

# Imports for using ini files.
from ConfigParser import ConfigParser

# Imports for reading and writing zip files.
from zipfile import ZipFile, ZIP_DEFLATED

if platform == "win32":
    from win32com.shell import shell, shellcon
else:
    import os

#-------------------------------------------------------------------------------

class BandwidthCounter(object):
    """
    A class for getting bandwidth usage.
    """
    
    def __init__(self):
        self.value = 0
        
    def __iadd__(self, x):
        self.value += x
        return self

#-------------------------------------------------------------------------------

class ContactsBackup(object):
    """
    Main class for backing up contacts.
    """
    
    API_KEY = 'YOUR_API
