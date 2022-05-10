import ctypes
# Test ctypes.CField instance
print ctypes.CField.__doc__

print ctypes.CField.offset
print ctypes.CField.__setattr__.__doc__

import sys
if sys.platform == 'cli':
    import clr
    print ctypes.CField.idx
    print ctypes.CField.__getattribute__.__doc__
    print ctypes.CField.name
    print ctypes.CField.pack

# from ctypes/test/test_structures.py
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_ubyte * 2), # 3
                ('b', ctypes.c_uint, 2),
                ('c', ctypes.c_ubyte * 2), # 2
                ('d', ctypes.c_uint, 2)]

testobj = X()
testobj.a = "\x1" * 2
testobj.c = "\x2" * 2
testobj.d = 0xe
testobj.b = 0xb
print testobj.a
print testobj.
