import ctypes
# Test ctypes.CFUNCTYPE()
# Also test that ctypes.CFUNCTYPE() can handle a function returning
# a pointer to a primitive type.
from ctypes import *
get_char_p = CFUNCTYPE(POINTER(c_char))(lambda: "foo")
if get_char_p() != "foo":
    raise RuntimeError, "CFUNCTYPE test failed"

print "OK"
