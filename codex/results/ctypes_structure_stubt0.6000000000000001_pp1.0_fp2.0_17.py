import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class P(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

print("S:", ctypes.sizeof(S))
print("P:", ctypes.sizeof(P))
# S: 8
# P: 8

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class P(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

print("S:", ctypes.sizeof(S))
print("P:", ctypes.sizeof(P))
# S: 8
# P: 8

class S(ctypes.Structure):
    _fields_ = [("x",
