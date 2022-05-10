import ctypes
# Test ctypes.CField
assert ctypes.CField._length_ is None
assert ctypes.CField._type_ is None
assert ctypes.CField._offset_ is None
assert ctypes.CField._name_ is None
assert ctypes.CField._pack_ is None
assert ctypes.CField._bits_ is None
assert ctypes.CField._index_ is None
f = ctypes.CField(ctypes.c_int, "field_name")
assert f._length_ is None
assert f._type_ is ctypes.c_int
assert f._offset_ is None
assert f._name_ == "field_name"
assert f._pack_ == 1
assert f._bits_ is None
assert f._index_ is None

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

try:
    A._fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
except Exception as e:
    assert type(e) is AttributeError
    assert str(e) == "
