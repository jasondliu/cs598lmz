import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # just to avoid a warning

class from_c(object):
    f = lambda self: None

def test(msg, got, expected):
    print msg, repr(got.f), repr(expected.f)
    try:
        assert got.f == expected.f
    except AssertionError:
        raise

if not hasattr(ctypes, "c_wchar"):
    # Needed to create a _fields_ item of the right type
    raise ImportError("need c_wchar")

ctypes.CFuncPtr.from_param(from_c()) # just to avoid a warning
ctypes.CFuncPtr.from_param(from_c()) # just to exercise the code

from ctypes import _CFuncPtr
from ctypes import _CFuncPtr_Cache
from ctypes import _CFuncPtr_Type

cases = [
    # Test if the hash does not blow up when passed non-hashable args
    ((_CFuncPtr, 'from_param'), {
            "obj": ctypes.CFuncPtr((), ctypes.c_int),
