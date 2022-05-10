import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import weakref

if sys.platform.startswith("win"):
    import win32api
    import pywintypes
    win32api.LoadLibrary("shlwapi.dll")

