import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time

monotonic_time_lib = ctypes.util.find_library('rt')
if monotonic_time_lib is not None:
    monotonic_time_lib = ctypes.CDLL(monotonic_time_lib)
    clock_gettime = lambda clk_id: monotonic_time_lib.clock_gettime(clk_id, ctypes.c_void_p(0))

a = clock_gettime(3)
def get_monotonic_time():
    if monotonic_time_lib is not None:
        a = clock_gettime(3)
        return a
    else:
        return time.time()

from tornado import web, ioloop
from tornado.websocket import WebSocketHandler

from sender import Sender
import db
from rightnow import RightNow

from web.forms import *
from web.handlers import *
from web.debug import *
from web.job import *
from web.base_handler import *

from util.crawl import *

