import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(2)
    y = ctypes.c_long(2)
    z = ctypes.c_long(2)
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ("z", ctypes.c_long)]

s = S()
print s.x
print s.y
print s.z

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ("z", ctypes.c_long)]

s = S()
s.x = 3
s.y = 4
s.z = 5
print s.x
print s.y
print s.z

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ("z", ctypes.c_long)]

s = S()
s.x = 3
s.
