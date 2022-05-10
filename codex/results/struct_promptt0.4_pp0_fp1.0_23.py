import _struct
# Test _struct.Struct

import _testcapi

# Create a test string for pack/unpack
teststring = "abcdefghijklmnop"

# Test native byte order
for code in 'bBhHiIlLqQ':
    s = _struct.Struct(code)
    assert s.size == _struct.calcsize(code)
    assert s.pack(42) == _struct.pack(code, 42)
    assert s.unpack(_struct.pack(code, 42)) == (42,)
    assert s.unpack_from(teststring, 0) == (ord(teststring[0]),)
    assert s.unpack_from(teststring, 1) == (ord(teststring[1]),)

# Test non-native byte order
for code in '@=<>!':
    for c in 'bBhHiIlLqQ':
        s = _struct.Struct(code + c)
        assert s.size == _struct.calcsize(code + c)
        assert s.pack(42) == _struct.pack(code + c, 42)
