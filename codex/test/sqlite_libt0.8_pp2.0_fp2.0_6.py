import ctypes
import ctypes.util
import threading
import sqlite3
import itertools
import logging
from logging.handlers import CEFHandler
import socket
import subprocess
import datetime
import calendar
import time
import json
import re
import os
import sys
import traceback
import platform
import syslog
import logging.handlers
import math
import struct

# vars for loop()
SOCKET_BUFFER_SIZE = 4096    # how much data to read from the server each time
SOCKET_TIMEOUT = 250         # how long to block waiting for data from the server
NOTIFY_INTERVAL = 60         # how often to send a notification to the server
NOTIFY_INTERVAL_GRACE = 5    # grace period after the last intent update to send a notification
# max notification size in bytes, including the null terminator
MAX_NOTIFICATION_SIZE = (ctypes.sizeof(ctypes.c_char) * 1024 * 1024) + ctypes.sizeof(ctypes.c_char)
KEEPALIVE_TIMEOUT = 100      # number of seconds to wait before sending another keepalive

# vars for control_loop()
