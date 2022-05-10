import ctypes
# Test ctypes.CFields

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

print X.a
print X.b

X._fields_ = [("a", ctypes.c_int)]
print X.a
print X.b

try:
    X._fields_ = [("a", ctypes.c_int),
                  ("b", ctypes.c_int),
                  ("c", ctypes.c_int)]
except ValueError:
    print "ValueError"

try:
    X._fields_ = [("a", ctypes.c_int),
                  ("b", ctypes.c_int),
                  ("c", ctypes.c_int),
                  ("d", ctypes.c_int)]
except ValueError:
    print "ValueError"

try:
    X._fields_ = [("a", ctypes.c_int),
                  ("b", ctypes.c_int),
                  ("c", ctypes.c_int),
                 
