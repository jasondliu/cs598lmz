import ctypes
# Test ctypes.CField.from_param

import ctypes
from ctypes import *

class C(Structure):
    _fields_ = [
        ("val", c_int),
        ("str", c_char_p),
    ]

    def __init__(self, val, str):
        super(C, self).__init__()
        self.val = val
        self.str = str

class D(Structure):
    _fields_ = [
        ("c", C),
    ]

    def __init__(self, val, str):
        super(D, self).__init__()
        self.c = C(val, str)

print "C(1, 'one')._as_parameter_"
print C(1, 'one')._as_parameter_

print "D(2, 'two')._as_parameter_"
print D(2, 'two')._as_parameter_
