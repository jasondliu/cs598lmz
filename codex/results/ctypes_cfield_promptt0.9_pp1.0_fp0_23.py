import ctypes
# Test ctypes.CField instances
import _ctypes_test
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char*10),
                ("c", ctypes.c_double)]
    _anonymous_ = [("d", ctypes.c_short),
                   ("e", ctypes.c_short)]
#    _anonymous_ = [("d", ctypes.c_short)]
#    _anonymous_ = [("e", ctypes.c_short)]
    _anonymous_ = [("foo", ctypes.c_char*10)]
    #raise ValueError("ouch")

print(X._fields_)
print([(name, type(getattr(X, name))) for name in dir(X) if name[0] != "_"])

class char4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char*4)]

print(char4._fields_)
print(char4.a)
print([(name, type(get
