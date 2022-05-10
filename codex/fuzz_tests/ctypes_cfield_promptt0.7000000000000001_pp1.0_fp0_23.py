import ctypes
# Test ctypes.CField

class CTest(ctypes.Structure):
    _fields_ = [
        ("_a", ctypes.c_int),
        ("_b", ctypes.c_int),
    ]
    a = ctypes.CField("_a")
    b = ctypes.CField("_b")

class CTest2(ctypes.Structure):
    a = ctypes.CField("_a")
    b = ctypes.CField("_b")
    _fields_ = [
        ("_a", ctypes.c_int),
        ("_b", ctypes.c_int),
    ]

class CTest3(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
    ]
    a = ctypes.CField("_a")
    b = ctypes.CField("_b")

class CTest4(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
       
