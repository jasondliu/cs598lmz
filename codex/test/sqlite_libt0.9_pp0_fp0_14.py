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

