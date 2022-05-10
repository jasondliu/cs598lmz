import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import time
import os
import sys
import re
import json

# TODO
# 1. 
# 2.

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class Dummy(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self
    def __getattr__(self, name):
        if self.kwargs.has_key(name):
            return self.kwargs[name]
        if self.args and len(self.args) > 0:
            return self.args[0]
        return self

class Logger(object):
    def __init__(self, log_
