import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import subprocess
import sys
import time
import re
import types

def load_library(libname):
    libname = ctypes.util.find_library(libname)
    if not libname:
        raise RuntimeError(
            "Could not find library %s" % libname
        )
    return ctypes.CDLL(libname)

def get_current_process_name():
    if sys.platform == 'win32':
        handle = ctypes.windll.kernel32.GetCurrentProcess()
        _, pid = ctypes.windll.kernel32.GetProcessId(handle)
        return os.path.basename(os.path.normpath(psutil.Process(pid).name()))
    else:
        return os.path.basename(os.path.normpath(psutil.Process().name()))

def get_process_list():
    ps = []
    for p in psutil.process_iter():
        try:
            if p.is_running():
                process = {}
                process['
