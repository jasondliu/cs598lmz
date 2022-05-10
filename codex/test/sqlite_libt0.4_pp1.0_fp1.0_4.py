import ctypes
import ctypes.util
import threading
import sqlite3
import os

import logging
log = logging.getLogger(__name__)

def get_libc():
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.sigwait.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_void_p)]
    libc.sigwait.restype = ctypes.c_int
    return libc

class SignalHandler(threading.Thread):
    def __init__(self, sigset):
        super(SignalHandler, self).__init__()
        self.sigset = sigset
        self.libc = get_libc()
        self.daemon = True
        self.start()

    def run(self):
        while True:
            signo = ctypes.c_int()
            self.libc.sigwait(self.sigset, ctypes.byref(signo))
            log.info('Received signal %s', signo.value)
