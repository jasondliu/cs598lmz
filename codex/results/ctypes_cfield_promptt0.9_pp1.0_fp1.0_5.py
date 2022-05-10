import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]
assert hasattr(C, "getfield")
# Another generic test
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.CField) * 3]
assert len(list(C._fields_)) == 3


# ctypes.Structure uses __slots__
class C(ctypes.Structure):
    pass
try:
    C().xyz = 42
except AttributeError:
    pass

# test IFUNCTYPE with floats
try:
    from ctypes import IFUNCTYPE, c_double
except ImportError:
    pass
else:
    incomplete = IFUNCTYPE(None)
    func = incomplete(lambda x: x)
    assert func(c_double(0.0)) == 0.0
    assert incomplete._restype_ == type(None)
    assert incomplete._argtypes_ is None
    assert func._argtypes_ == [c_double]

# now tests that require a shared
