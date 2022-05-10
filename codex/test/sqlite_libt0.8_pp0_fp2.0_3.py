import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import unicodedata

# macOS
framework_path = ctypes.util.find_library('CoreFoundation')
objc = ctypes.cdll.LoadLibrary(framework_path)

# Linux
#objc = ctypes.CDLL('libobjc.so.4')

# Windows
#objc = ctypes.CDLL('libobjc.dll')


