import ctypes
import ctypes.util
import threading
import sqlite3
import fcntl
from personal.common.sleep_tools import *
from personal.common import check_pid

from personal.monitor import monitor
from personal.common import check_file, MyEvent, exit
from personal.common import open_device, open_file_from_fmt, BlockPrint, loge
from personal.common import pattern_get_from_db, pattern_from_fmt

from common import cfg

from personal.compile_patterns import patterns, compile_pattern, get_patt_features

from personal.common.pycompat import *
from enum import Enum
from personal.common.open_file_from_fmt import *

from personal.common.block_print import *
from personal.common.sleep_tools import *
from personal.common.check_pid import *

from personal.common.config import *
from personal.common.open_device import *
from personal.common.pattern_from_fmt import *
from personal.common.open_file_from_fmt import *


import re

def sync_db():
    conn
