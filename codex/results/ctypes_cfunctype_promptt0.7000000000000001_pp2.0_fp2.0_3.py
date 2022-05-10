import ctypes
# Test ctypes.CFUNCTYPE on a simple function.

import _ctypes_test

print('Testing ctypes.CFUNCTYPE')

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(_ctypes_test.fptr)
print(f(1))
print(f(2))

if repr(f) == "<ctypes.CFUNCTYPE(ctypes.c_int) object at 0x%x>" % (id(f),):
    print('repr(f) is OK')
else:
    print(repr(f))
    print('repr is bad!')
