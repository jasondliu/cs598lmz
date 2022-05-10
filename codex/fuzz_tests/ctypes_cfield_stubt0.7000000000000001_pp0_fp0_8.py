import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    pass

ctypes.CStruct = type(S2)

# now test some common ctypes.Structure methods
assert ctypes.sizeof(S) == ctypes.sizeof(S())
assert S().x == 0

s = S()
s.x = 1234
assert s.x == 1234
assert hash(s) == hash(S())

assert str(S) == "S"
assert repr(S) == "<class 'S'>"
assert repr(s) == "<S object at " + hex(id(s)) + ">"

assert len(S._fields_) == 1
assert S._fields_[0] == ("x", ctypes.c_int)
assert S._fields_ == S._fields_
assert S._fields_ != S2._fields_

assert issubclass(S, ctypes.Structure)
assert not issubclass(S, ctypes.Array)
assert isinstance(s, ctypes.Structure)
assert not isinstance(s, ctypes.Array)
