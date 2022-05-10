import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import re
import mmap

# TODO: use ctypes.sizeof(ctypes.c_wchar) when Python 2.6 is available
WCHAR_SIZE = 4

class DebuggerThread(threading.Thread):
    def __init__(self, debugger, process_handle, callback_func, db_filename,
                 loadlibrary_filter):
        self.debugger = debugger
        self.process_handle = process_handle
        self.callback_func = callback_func
        self.db_filename = db_filename
        self.loadlibrary_filter = loadlibrary_filter
        self.stopped = False
        self.db = None
        self.load_module_sql = None
        self.unload_module_sql = None
        self.load_module_info_sql = None
        self.insert_module_sql = None
        self.get_module_sql = None
        threading.Thread.__init__(self)
        
