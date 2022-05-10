import ctypes
# Test ctypes.CField.from_address
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

x = X()
fld = c_int.from_address(addressof(x))
fld.value = 1
if x.a != 1:
    raise RuntimeError

try:
    c_int.from_address(0)
except ValueError:
    pass
else:
    raise RuntimeError

try:
    c_int.from_address(addressof(x), 0)
except ValueError:
    pass
else:
    raise RuntimeError

try:
    c_int.from_address(addressof(x), 1)
except ValueError:
    pass
else:
    raise RuntimeError

try:
    c_int.from_address(addressof(x), 2)
except ValueError:
    pass
else:
    raise RuntimeError

fld = c_int.from_address(addressof(x), 0, 1)
fld.value = 1
if x.
