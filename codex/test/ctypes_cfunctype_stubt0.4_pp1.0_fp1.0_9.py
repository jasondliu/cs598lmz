import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

#------------------------------------------------------------------------------
# Test for the case where the return type is a pointer to a struct.
#------------------------------------------------------------------------------

import ctypes
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

FUNTYPE = ctypes.CFUNCTYPE(ctypes.POINTER(S))
