import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

# This is the same as:

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

print s.x, s.y

# You can also set the fields in the constructor:

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S(1, 2)

print s.x, s.y

# You can also use keyword arguments:

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S(x=1, y
