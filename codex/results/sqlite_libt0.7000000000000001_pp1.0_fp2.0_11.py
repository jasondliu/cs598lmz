import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import signal
import sys
import os
import subprocess
import socket
import glob

# logging
import logging

# config
from config import *

# rfid tools
from rfid_routines import *

# sqlite routines
from sqlite_routines import *

# other
from math import sqrt
from math import isnan

# set to true if we want to run in testing mode
TESTING = False

# set to true if we want to bypass RFID card reading
BYPASS_CARD_READING = False

# set to true if we want to use a watchdog timer
USE_WATCHDOG_TIMER = True


# set to true if we want to use a watchdog timer
USE_GPS = True


# set to true if we want to use a watchdog timer
USE_BLE = True


# set to true if we want to use a watchdog timer
USE_RELAY = True


# set to true if we want to use a watchdog timer
USE_TEMPERATURE = True


# set to true
