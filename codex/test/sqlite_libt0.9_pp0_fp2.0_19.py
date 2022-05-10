import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re
import math
import xml.etree.ElementTree as ET

from pymobility.models.mobility import *

# To print just time in a log message except for PrintLevel.ALL
log_timer = Timer()

