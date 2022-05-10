import ctypes
import ctypes.util
import threading
import sqlite3
import urllib2
import json
import hashlib
import os
import sys
import logging
import logging.handlers
import ConfigParser

from random import randint
from urlparse import urlparse
from urllib import unquote
from sys import argv, exit
from optparse import OptionParser

logging.basicConfig(level=logging.DEBUG)

# Get a AR-Drone library
def get_ar_drone_lib():
    """
    This function attempts to get an instance of the libARDrone library.
    It first attempts to load the library from a user-supplied
    location, and if this fails it falls back on ctypes.util.

    :return: The library, ready to use
    :rtype: ctypes.cdll
    """
    # Get the path from the CLI or default to the current folder
    if len(argv) > 1 and argv[1] is not None:
        path = argv[1]
    else:
        path = '.'

    # If path does not end in a / or \\, add one
    if
