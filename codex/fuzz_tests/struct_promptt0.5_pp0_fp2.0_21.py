import _struct
# Test _struct.Struct.__reduce__

import pickle

import _testcapi

def test_reduce():
    s = _struct.Struct("i")
    r = s.__reduce__()
    assert r == (s.__class__, ("i",), None)
    assert type(r[0]) is type(s.__class__)
    s2 = s.__new__(s.__class__)
    s2.__setstate__(r[1])
    assert s.format == s2.format

def test_reduce_with_buffer():
    s = _struct.Struct("i")
    b = buffer("abcdef")
    r = s.__reduce__(b)
    assert r == (s.__class__, ("i", b), None)
    assert type(r[0]) is type(s.__class__)
    s2 = s.__new__(s.__class__)
    s2.__setstate__(r[1])
    assert s.format == s2.format
    assert s2.un
