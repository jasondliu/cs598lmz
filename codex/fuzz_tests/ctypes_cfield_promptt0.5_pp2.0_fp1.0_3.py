import ctypes
# Test ctypes.CField
#
# This is a test for bug #1265395.

# The following code is a slightly modified version of the code in
# bug #1265395.

class S(ctypes.Structure):
    _fields_ = [("data", ctypes.c_uint32),
                ("flags", ctypes.c_uint32, 1),
                ("address", ctypes.c_uint32, 31)]

s = S()
s.flags = 1

print s.flags
print s.address
print s.data
