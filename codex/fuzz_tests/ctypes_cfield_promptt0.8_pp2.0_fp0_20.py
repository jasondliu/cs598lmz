import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte, 3),
                ("s", ctypes.c_short),
                ("i", ctypes.c_int)]

ctypes.sizeof(C)

C._pack_ = 1

ctypes.sizeof(C)

class C(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte, 3),
                ("s", ctypes.c_short),
                ("i", ctypes.c_int, 2)]

ctypes.sizeof(C)

C._pack_ = 1

ctypes.sizeof(C)

class C(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte, 3),
                ("s", ctypes.c_short),
                ("i", ctypes.c_int, 2)]

C._pack_ = 2

ctypes.sizeof(C)

class C(ctypes.Structure):
    _fields_
