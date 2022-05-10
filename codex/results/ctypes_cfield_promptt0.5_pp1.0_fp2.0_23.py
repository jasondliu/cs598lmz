import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("x", ctypes.c_int)]

t = T(S(1, 2), 3)
print t.s.a, t.s.b, t.x

# Test ctypes.CField.from_address
# This test is not implemented yet
#print "from_address"
#t2 = ctypes.CField.from_address(ctypes.addressof(t), T)
#print t2.s.a, t2.s.b, t2.x

# Test ctypes.CField.from_buffer
print "from_buffer"
t3 = ctypes.CField.from_buffer(ctypes.c_buffer("abcdefghijklmnopqrstuvwx"), T)
print t3.s.a, t3.s.b, t3.
