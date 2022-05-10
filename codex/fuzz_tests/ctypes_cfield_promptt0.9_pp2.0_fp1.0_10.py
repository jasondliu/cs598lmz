import ctypes
# Test ctypes.CField.from_address()

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]

obj = X()
print(type(X.from_address(addressof(obj)).a))
print(ctypes.c_long.from_address(addressof(obj)).a)
X.from_address(addressof(obj)).a = 12
assert obj.a == 12, obj.a
X.from_address(addressof(obj)).b = 99
assert obj.b == 99, obj.b
from array import array
from ctypes import *
from ctypes.test.test_pickling import XY, XYZ

# The following is a regression test: array.frombytes was able to
# access buffer of ctypes instance at array creation. The
# memoryview.cast interface introduced in Py3.3 makes this impossible,
# as ctypes instance don't provide memoryviews.
#
# The problem is that if 'own' is true, array() will release the
# memoryview, which then releases
