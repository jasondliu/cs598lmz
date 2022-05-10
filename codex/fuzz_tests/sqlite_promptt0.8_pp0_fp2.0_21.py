import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
import time
import os
import sys
import socket
import errno
import multiprocessing
import copy
# import pprint

lib = ctypes.CDLL(ctypes.util.find_library('pthread'), use_errno=True)

def prctl(cmd, arg2):
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    ret = libc.prctl(cmd, arg2)
    if ret != 0:
        raise OSError(ctypes.get_errno())

class Thread(threading.Thread):
    """
    This thread is responsible for calling the worker process.
    """

    def __init__(self, target, args, daemon=True):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args
        self._daemon = daemon
        self.setDaemon(True)
        self.worker = None
        self.queue = Queue()
        self
