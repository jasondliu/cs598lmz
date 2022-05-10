import ctypes
# Test ctypes.CField
class StructA(ctypes.Structure):
    _fields_ = [
        ("Field1", ctypes.c_uint32),
        ("Field2", ctypes.c_uint32),
        ("Field3", ctypes.c_uint32),
    ]

class StructB(ctypes.Structure):
    _fields_ = [
        ("Field4", ctypes.c_uint32),
        ("Field5", ctypes.c_uint32),
        ("Field6", ctypes.c_uint32),
    ]

class StructC(ctypes.Structure):
    _fields_ = [
        ("Field7", ctypes.c_uint32),
        ("Field8", ctypes.c_uint32),
        ("Field9", ctypes.c_uint32),
    ]

class StructD(ctypes.Structure):
    _fields_ = [
        ("StructA", ctypes.CField(StructA)),
        ("StructB", ctypes.CField(StructB)),
        ("StructC", ctypes.CField(StructC)),

