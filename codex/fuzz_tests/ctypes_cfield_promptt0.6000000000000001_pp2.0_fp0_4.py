import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __str__(self):
        print "test"
        return "test"

p = Point(1, 2)
print p.x, p.y

# Test ctypes.CField.from_param
# Test ctypes.CField.in_dll
# Test ctypes.CField.offset
# Test ctypes.CField.set
# Test ctypes.CField.get
# Test ctypes.CField.__get__
# Test ctypes.CField.__set__
# Test ctypes.CField.__delete__
# Test ctypes.CField.__init__

# Test ctypes.CField.from_address
# Test ctypes.CField.from_buffer
# Test ctypes.CField.in_dll
# Test ctypes.CField.offset
# Test ctypes.CField.set
# Test ctypes.CField.get
# Test ctypes.C
