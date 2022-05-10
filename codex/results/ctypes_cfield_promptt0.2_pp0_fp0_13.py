import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("a", POINT),
                ("b", POINT)]

r = RECT()
r.a.x = 1
r.a.y = 2
r.b.x = 3
r.b.y = 4
print(r.a.x, r.a.y, r.b.x, r.b.y)

# Test ctypes.CField.from_param
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("a", POINT),
                ("b", POINT)]

r = RECT()
r.a.x = 1
r.a.y = 2
r.b.x = 3
