import ctypes
import ctypes.util
import threading
import sqlite3
from multiprocessing import Pool
import sys
from Queue import Empty
from time import sleep
from uuid import uuid4
from datetime import datetime
import logging

logger = logging.getLogger('mmr')

class MMRError(Exception): pass
class MMR_NOT_INITIALIZED(MMRError): pass

class MMR(object):

    ALIVE = True
    DEAD = False
    STATE = ALIVE

    FULL = -1
    SAME = 0
    DIFF = 1

    def __init__(self, fname=None, keep_alive=True, caching=True, sync_cache=True, **kwargs):
        """
        Initializes FImR object

        Parameters:
        :param str fname: sqlite3 database filename
        :param str mode: open mode to pass to sqlite3.connect()
        :param bool keep_alive: whether `keep_alive` thread should be started. If False, no blocks will be retrieved until `.start_keep_alive()` is called.
        :param bool
