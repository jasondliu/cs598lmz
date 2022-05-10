import ctypes
# Test ctypes.CField structure
class x(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
print x._fields_

# Test ctypes.Field structure
class x(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
p = x()
print p.__dict__.keys()
print p._fields_

# Test ctypes.Union Fields structure
class x(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
print x._fields_

# Test ctypes.pointer Fields structure
class x(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
p = ctypes.pointer(x())
print p.contents.__dict__.keys()
print p.contents._fields_
