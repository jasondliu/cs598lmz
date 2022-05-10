import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect vs. sqlite3.Connection
# sqlite3.connect returns a Connection instance, which is what we really want
# db = sqlite3.connect(':memory:')
# sqlite3.Connection.


import logging
log = logging.getLogger('fixgw.fix_interface')

from fixt.fix_42 import Fix42
from fixt.codecs import Codec

from fixgw.engine import FixEngine, FixMsg
from fixgw.constants import *


_quickfix = ctypes.util.find_library('quickfix')
