import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import struct 
import time
import collections
import xml.etree.cElementTree as ElementTree

# Global variable
dllname = ""
dllpath = ctypes.util.find_library("xwords4")
if not dllpath:
    dllpath = ctypes.util.find_library("xwords.dll")
if dllpath:
    dllname = dllpath
    xwc = ctypes.cdll.LoadLibrary(dllname)
#xwc = ctypes.cdll.LoadLibrary("/home/luebke/Desktop/PyXWords/xwords/xwords.dll")
#xwc = ctypes.cdll.LoadLibrary("/home/luebke/code/xwords4/xwords4/xwords4.dll")

XW_TILES_VISIBLE = 0
XW_TILES_HIDDEN = 1
XW_TILES_ALL = 2

XW_TRAY_ALL = 0
XW_TRAY_USER = 1

# init
x
