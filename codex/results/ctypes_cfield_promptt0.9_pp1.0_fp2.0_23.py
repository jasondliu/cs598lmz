import ctypes
# Test ctypes.CField
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('tag', ctypes.CField)] # Bad ctypes.CField
print POINT

# ctypes.CField must be used in Structure
import ctypes
print ctypes.CField

# ctypes.CField must be used in Structure
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

print POINT
print POINT.tag

# ctypes.Pointer must be used in pointer
import ctypes
p = ctypes.Pointer(1) # Bad use of ctypes.Pointer
print p
print len(p)

# Test of polymorphic class
class Array:
    def __init__(self):
        self._data = [0, 1, 2, 3, 4]
    def __getitem__(self, i):
       
