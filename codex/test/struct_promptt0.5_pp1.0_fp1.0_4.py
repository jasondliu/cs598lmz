import _struct
# Test _struct.Struct.sizeof()

import _struct

def test_sizeof():
    # Test _struct.Struct.sizeof()
    s = _struct.Struct('hhl')
    assert s.size == _struct.calcsize('hhl')
    assert s.size == s.sizeof()
    s = _struct.Struct('>hhl')
    assert s.size == _struct.calcsize('>hhl')
    assert s.size == s.sizeof()

def test_compare():
    # Test comparison of _struct.Struct objects
    s1 = _struct.Struct('hhl')
    s2 = _struct.Struct('hhl')
    s3 = _struct.Struct('>hhl')
    assert s1 == s2
    assert s1 != s3
    assert s1 < s3
    assert s3 > s1
    assert s1 <= s2
    assert s1 <= s3
    assert s3 >= s1
    assert s2 >= s1

