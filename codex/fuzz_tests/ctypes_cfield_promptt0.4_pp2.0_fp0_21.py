import ctypes
# Test ctypes.CField
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField)]

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField),
                ("d", ctypes.CField)]

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField),
                ("d", ctypes.CField),
                ("e", ctypes.CField)]

class U
