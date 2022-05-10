import ctypes
# Test ctypes.CField()
class POINT(ctypes.Structure):
    _fields_ = (('x', ctypes.c_int),
                ('y', ctypes.c_int))

p = POINT()
p.x = 1
p.y = 2
print(p.x)
print(p.y)

class POINT2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

p = POINT2()
p.x = 1
p.y = 2
print(p.x)
print(p.y)

# ctypes.CField can improve speed a little bit, but wastes memory.

# Test ctypes.POINTER()
# use default_args, this is an advanced usage.
class Py_buffer2(ctypes.Structure):
    _fields_ = [ ('buf', ctypes.POINTER(None)) ]

Py_buffer2._fields_[0][1]._type_ = ctypes.c_char * 8

buf2 = Py
