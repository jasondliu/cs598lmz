import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]
print POINT.x.offset
print POINT.y.offset

# Test ctypes.c_buffer
class BUFFER(ctypes.Structure):
    _fields_ = [("buf", ctypes.c_buffer(10))]

#print BUFFER.buf.offset

# Test ctypes.CDLL
cdll = ctypes.CDLL("./libpy.so")
print cdll.pyobject_hash()

# Test ctypes.c_char_p
print cdll.pyobject_as_string(cdll.pyobject_hash())

# Test ctypes.c_int
print cdll.pyobject_type(cdll.pyobject_hash())

# Test ctypes.c_void_p()
print cdll.pyobject_hash()

# Test ctypes.byref
print cdll.pyobject_as_string(ctypes.byref(ctypes.
