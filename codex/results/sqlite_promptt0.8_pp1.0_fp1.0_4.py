import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections connection.
from sqlite3.test.test_threading import RLock
from sqlite3 import dbapi2 as sqlite

from pymavlink import mavutil
import os
from time import sleep

# Not using aero_server, but using aero_position code from aero_server
from aero_position import AeroPosition
from aero_log_to_sqlite import AeroLogToSqlite
#from aero_position_client import AeroPositionClient


# Get constants from AeroCommander server
from AeroCommander import *

# Create a logger
from aero_logger import AeroLogger
our_logger = AeroLogger(__name__, "/tmp/aero_monitor_py.log")

# Need to do this if running twice in same process
#src_path = [os.path.dirname(aero_server)]
#if src_path[0] not in sys.path:
#    sys.path.insert(0, os.path.dirname(aero_server))
#from aero_log_to_sqlite import Aero
