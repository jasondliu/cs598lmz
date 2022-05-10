import ctypes
# Test ctypes.CField pointer type.

import ctypes
class TestCField(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int),
                ("pvalue", ctypes.POINTER(ctypes.c_int))]

print TestCField

t = TestCField(1, None)

# This fails because t.pvalue is not initialised
#print t.pvalue.contents

t.pvalue = ctypes.pointer(ctypes.c_int(2))
print t.pvalue.contents

print t.value, t.pvalue.contents.value
