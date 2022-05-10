import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure
    x.y = ctypes.BigEndianStructure
    x.z = ctypes.LittleEndianStructure
    x.w = ctypes.Union

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.Structure)]
    x.y = ctypes.BigEndianStructure
    x.z = ctypes.LittleEndianStructure
    x.w = ctypes.Union

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ulong), ("b", ctypes.c_byte), ("c", ctypes.c_uint)]

class Y(ctypes.Structure):
    _fields_ = [("x", ctypes.Structure), ("y", ctypes.Structure)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ulong), ("b", ctypes.c_ubyte), ("c", ctypes.c_uint)]
    x = ctypes.Union([("a
