import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
from pprint import pprint
import datetime
from modules.module_base import ModuleBase
from modules.module_util import get_module_config, get_module_class
from modules import db_util
from modules.module_base import ModuleRegistry
import modules.module_util as module_util

from fcntl import ioctl
from pyroute2 import IPRoute
from pyroute2 import protocols
from pyroute2 import NetlinkError


clib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

#
# define constants.
#
SIOCGIFHWADDR = 0x8927  # Get hardware address
SIOCGIFADDR  = 0x8915   # Get PA address

class sockaddr(ctypes.Structure):
    _fields_ = [("sa_family", ctypes.c_short),
                ("sa_data", ctypes.c_char * 14)]

