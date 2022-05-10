import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import re
import sys

# The following function is from http://www.dalkescientific.com/writings/diary/archive/2005/04/20/tracing_python_code.html
def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_globals["__name__"]
        line = linecache.getline(filename, lineno)
