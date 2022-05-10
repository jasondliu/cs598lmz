import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int)]

class C2(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class C3(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class C4(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int)]

class C5(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int), ('v', ctypes.
