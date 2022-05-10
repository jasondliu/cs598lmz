import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import logging

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

class FileHook(object):
    def __init__(self, file_path, file_name, hits):
        self.file_path = file_path
        self.file_name = file_name
        self.hits = hits

    def __repr__(self):
        return 'FileHook(%s, %s, %d)' % (self.file_path, self.file_name, self.hits)

class FileSystemHook(object):
    def __init__(self, file_path, file_name, hits, offset, data):
        self.file_path = file_path
        self.file_name = file_name
        self.hits = hits
        self.offset = offset
        self.data = data

