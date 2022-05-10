import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import subprocess
import sys

# class definition
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

