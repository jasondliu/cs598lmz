import ctypes
# Test ctypes.CField.
import ctypes
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_short),
                ('c', ctypes.c_byte)]
# The struct module's alignment attribute is a sizeof(void*) aligned
# integer, which may not match the alignment of a C pointer.  The
# value is always greater than the alignment of a C pointer, so
# subtracting sizeof(void*) should make it smaller.
import struct, ctypes
assert struct.calcsize('P') == ctypes.sizeof(ctypes.c_voidp)
assert struct.calcsize('P') > struct.calcsize('c')
assert struct.calcsize('P') > struct.calcsize('b')
assert struct.calcsize('P') > struct.calcsize('h')
assert struct.calcsize('P') > struct.calcsize('i')
assert struct.calcsize('P') > struct.calcsize('l')
assert struct.calcsize('P') > struct.cal
