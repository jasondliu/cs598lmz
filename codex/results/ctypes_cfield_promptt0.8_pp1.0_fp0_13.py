import ctypes
# Test ctypes.CField.from_param()
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

if lib.TestFunc2.argtypes is None:
    raise ctypes.ArgumentError("TestFunc2", "expected an argument")

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_longl
