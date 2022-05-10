import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import logging
import time
import datetime


def find_lib():
    return find_library("c")

def open(self, filename, mode, uri):
    ext = os.path.splitext(filename)[1]
    if ext != '.sqlite':
        raise ValueError("Unsupported File Extension")
    self.con = sqlite3.connect(filename)

def read_line(self):
    return next(self.con)


def readline(self):
    return next(self.con)

def key_exists(dict, key):
    if key in dict:
        return True
    else:
        return False

table_creates = {}
table_creates["borders"] = """CREATE TABLE IF NOT EXISTS borders(x integer, y integer, z integer, chunk_x integer, chunk_y integer, chunk_z integer);"""
