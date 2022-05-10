import ctypes
# Test ctypes.CFUNCTYPE, see http://docs.python.org/library/ctypes.html
import struct, sys
if sys.byteorder == 'little':
    def endian(i, swapped):
        if swapped:
            return struct.unpack('h', struct.pack('H', i))[0]
        else:
            return i
else:
    def endian(i, swapped):
        if swapped:
            return struct.unpack('H', struct.pack('h', i))[0]
        else:
            return i

# make a function that does nothing
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
def c_func(self, a, b, lena, lenb, swapped, data):
    pass
c_func = CMPFUNC(c_func)

