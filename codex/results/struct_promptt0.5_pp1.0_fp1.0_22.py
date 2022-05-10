import _struct
# Test _struct.Struct.__repr__()
with support.check_py3k_warnings(quiet=True):
    s = _struct.Struct('i')
    expected = '<_struct.Struct object at 0x{:x}>'.format(id(s))
    assert repr(s) == expected
    s = _struct.Struct('i')
    expected = '<_struct.Struct object at 0x{:x}>'.format(id(s))
    assert repr(s) == expected
    s = _struct.Struct('')
    expected = '<_struct.Struct object at 0x{:x}>'.format(id(s))
    assert repr(s) == expected
    s = _struct.Struct('=')
    expected = '<_struct.Struct object at 0x{:x}>'.format(id(s))
    assert repr(s) == expected


# Test _struct.Struct.__sizeof__()
with support.check_py3k_warnings(quiet=True):
    s = _struct.Struct('i')
    assert s.__size
