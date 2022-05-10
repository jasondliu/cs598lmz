import _struct
# Test _struct.Struct.__module__
s = _struct.Struct('i')
assert s.__module__ == '_struct'
assert repr(s).startswith("<class '_struct.Struct'>")

import copy
# Test copy.deepcopy()
try:
    copy.deepcopy(s)
except TypeError:
    pass
else:
    assert 0, "deepcopy() should fail"

# Test PyCapsule
import _testcapi
c = _testcapi.PyCapsule_New(b'hello', b'test', None)
s = _struct.Struct(b'P')
packed = s.pack(c)
assert packed == b'\x00\x00\x00\x00\x00\x00\x00\x00'
assert s.unpack(packed) == (c,)

# Test pointer
p = _testcapi.PyCapsule_GetPointer(c, b'test')
assert p == b'hello'
assert _testcapi.PyCapsule_GetName(c) == b'test'
assert
