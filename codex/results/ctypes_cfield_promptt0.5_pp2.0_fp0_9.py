import ctypes
# Test ctypes.CField.from_address
from ctypes import *

class S(Structure):
    _fields_ = [("x", c_int)]

p = pointer(S())
p.contents.x = 42

if p.contents.x != 42:
    raise RuntimeError

q = c_int.from_address(addressof(p.contents))
if q.value != 42:
    raise RuntimeError

q.value = 99
if p.contents.x != 99:
    raise RuntimeError

# Test that a c_char_p instance can be initialized from a Python string
from ctypes import *
c_char_p("abc")

# Test that a c_char_p instance can be initialized from a Python unicode string
from ctypes import *
c_char_p(u"abc")

# Test that a c_char_p instance can be initialized from a Python buffer
from ctypes import *
c_char_p(b"abc")

# Test that a c_wchar_p instance can be initialized from a Python unicode string
from c
