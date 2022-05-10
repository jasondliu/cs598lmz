import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("_x", ctypes.c_int),
                ("_y", ctypes.c_int)]

s = S()
s.x = 10
print s.x
print s._fields_
print s.__dict__
print s.__dict__["_x"]
print s.__dict__["_y"]
