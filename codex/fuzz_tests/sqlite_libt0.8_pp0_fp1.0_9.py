import ctypes
import ctypes.util
import threading
import sqlite3
import os

class Segment:
    def __init__(self, path):
        self.lib = ctypes.cdll.LoadLibrary(path)

    def analyze(self, text):
        self.lib.analyze.restype = ctypes.c_char_p
        return self.lib.analyze(text)

    def analyze_init(self):
        self.lib.analyze_init.restype = ctypes.c_void_p
        return self.lib.analyze_init()

    def analyze_exit(self, p):
        self.lib.analyze_exit(p)

    def analyze_with_start(self, p, text):
        self.lib.analyze_with_start.restype = ctypes.c_char_p
        return self.lib.analyze_with_start(p, text)

    def free_mem(self, p):
        self.lib.free_mem(p)

class Job:
    def __init__(self, text, p, tid):
        self.text = text
        self
