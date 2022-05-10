import ctypes
# Test ctypes.CField
class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

cf = CField()
cf.a = ctypes.c_char_p("hello")
cf.b = ctypes.c_char_p("world")
print(cf.a, cf.b)

# Test ctypes.CField
class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

cf = CField()
cf.a = ctypes.c_char_p("hello")
cf.b = ctypes.c_char_p("world")
print(cf.a, cf.b)


# Test ctypes.CField
class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

cf = CField()
cf.a =
