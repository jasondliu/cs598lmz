import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re

THREADS = 12

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorWrap(string, color):
    return color + string + bcolors.ENDC

class LibcTraverser(object):
    def __init__(self, libc):
        self.libc = libc

    def traverse(self):
        cnt = 0
        for f in dir(self.libc):
            fnc = getattr(self.libc, f)
            if hasattr(fnc, "__call__"):
                cnt += 1
                print(f)
