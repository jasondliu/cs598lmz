import ctypes
# Test ctypes.CFUNCTYPE
print ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x)

# Test ctypes.Structure.__new__()
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
print POINT()
print POINT(1, 2)

# Test ctypes.Structure.__init__()
class Rect(ctypes.Structure):
    _fields_ = [('upperleft', POINT), ('lowerright', POINT)]
print Rect(POINT(1, 2), POINT(3, 4))
print Rect(POINT(1, 2), lowerright=POINT(3, 4))
print Rect(upperleft=POINT(1, 2), lowerright=POINT(3, 4))

# Test ctypes.Structure.__repr__()
print Rect((1, 2), (3, 4))

# Test ctypes.Union.__new__()
class UNION(ctypes.Union):
    _fields_ = [
