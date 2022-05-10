import ctypes
ctypes.cast(0, ctypes.py_object)

import ctypes
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(id))

import ctypes
ctypes.cast(id, ctypes.c_void_p).value
######

import ctypes  ##for calling GetForegroundWindow() and some other functions from user32.dll
user32 = ctypes.windll.user32

import win32gui  #for creating transparent window
import win32con
import win32process

import time

#create a transparent window
window = win32gui.FindWindow(None, "Dialog name")
windowRect = win32gui.GetWindowRect(window)
title = ""
hWnd = win32gui.CreateWindowEx(
    win32con.WS_EX_COMPOSITED,   # So it is on top
