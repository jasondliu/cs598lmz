import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16
    y = ctypes.c_int16

class T(ctypes.Structure):
    _pack_ = 2
    s = S

a = (T * 2)()
a[0].s.x = 0
a[0].s.y = 1
a[1].s.x = 2
a[1].s.y = 3

import pprint
pprint.pprint(a[:])
#Traceback (most recent call last):
#Failure: (expected: 0; actual: 0)
#ValueError: ctypes object at 0x0x32cfa00 has incorrect size: should be 16, but is 32

#value error
