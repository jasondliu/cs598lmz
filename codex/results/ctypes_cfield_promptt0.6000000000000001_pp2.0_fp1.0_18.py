import ctypes
# Test ctypes.CField
class TestCFied(ctypes.Structure):
    _fields_ = [("a", ctypes.c_float),
                ("b", ctypes.c_float)]

class TestCFied2(ctypes.Structure):
    _fields_ = [("c", ctypes.c_float)]

class TestCFied3(ctypes.Structure):
    _fields_ = [("d", ctypes.c_float)]

class TestCFied4(ctypes.Structure):
    _fields_ = [("e", ctypes.c_float)]

class TestCFied5(ctypes.Structure):
    _fields_ = [("f", ctypes.c_float)]

class TestCFied6(ctypes.Structure):
    _fields_ = [("g", ctypes.c_float)]

class TestCFied7(ctypes.Structure):
    _fields_ = [("h", ctypes.c_float)]

class TestCFied8(ctypes.Structure):
    _fields_ = [("i", ctypes.c_
