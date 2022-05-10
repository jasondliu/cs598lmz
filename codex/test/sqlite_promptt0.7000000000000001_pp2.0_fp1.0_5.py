import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

#import struct
#import binascii
#import array
#import socket

#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s\t%(module)s.%(funcName)s: %(message)s', datefmt='%H:%M:%S')

_libc = ctypes.CDLL(ctypes.util.find_library('c'))

#

def os_getpid():
    return _libc.getpid()

def os_fork():
    pid = _libc.fork()
    if pid == -1:
        raise OSError
    return pid

def os_lockf(fd, cmd, len):
    return _libc.lockf(fd, cmd, len)

#

class Lock(object):
    def __init__(self):
        self._lock = threading.Lock()
        #self.owner = None

