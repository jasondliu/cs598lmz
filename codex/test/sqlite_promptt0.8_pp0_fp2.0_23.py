import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.uic as QtUiTools

if not hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):
    def Py_InitModule4_64(name, methods, doc, passthrough, apiver):
        return ctypes.pythonapi.Py_InitModule4(
            name, methods, doc, passthrough, apiver)
else:
    Py_InitModule4_64 = ctypes.pythonapi.Py_InitModule4_64

_C_API = None

def install():
    global _C_API
    if _C_API is None:
        _C_API = PyCapsule_New(ctypes.pythonapi.PyThreadState_GetDict(),
                             None, None)
