import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error
import os.path
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import subprocess
import signal
import sys
import time
import re
import json
import socket
import struct
import fcntl
from enum import Enum
from collections import namedtuple

#
# Global variables
#

# sqlite3 database connection
db_conn = None

# sqlite3 cursor
db_cursor = None

# logging
logger = None

#
# Enums
#

class InterfaceType(Enum):
    """
    Enumeration of the different types of interfaces
    """
    WIRED = 1
    WIFI = 2
    BLUETOOTH = 3

class InterfaceState(Enum):
    """
    Enumeration of the different states of interfaces
    """
    UP = 1
    DOWN = 2
    UNKNOWN = 3

class InterfaceMode(Enum):
    """
    Enumeration of the different modes of interfaces
    """
    MASTER =
