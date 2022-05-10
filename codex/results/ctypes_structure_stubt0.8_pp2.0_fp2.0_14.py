import ctypes

class S(ctypes.Structure):
    x = 1
    ctypes_version = tuple(ctypes.__version__.split('.'))
    if ctypes_version >= ('1','1','0'):
        _pack_ = 2
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

# Create a structure instance and set the attributes
s = S()
s.a = 65
s.b = 66

# Create a pointer to the structure, and set its contents
p = ctypes.pointer(s)
p.contents.a = 67
p.contents.b = 68

print s.a, s.b
print p.contents.a, p.contents.b
