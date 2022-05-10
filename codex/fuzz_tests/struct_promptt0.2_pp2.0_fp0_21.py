import _struct
# Test _struct.Struct.

def test_struct_format():
    # Test that the format string is checked for validity.
    try:
        _struct.Struct('x')
    except ValueError:
        pass
    else:
        raise TestFailed, '_struct.Struct("x") did not raise ValueError'

def test_struct_size():
    # Test that the size is calculated correctly.
    s = _struct.Struct('i')
    if s.size != _struct.calcsize('i'):
        raise TestFailed, '_struct.Struct("i").size returned %d, expected %d' % \
              (s.size, _struct.calcsize('i'))

def test_struct_pack():
    # Test that packing works correctly.
    s = _struct.Struct('i')
    if s.pack(12345) != _struct.pack('i', 12345):
        raise TestFailed, '_struct.Struct("i").pack(12345) returned %s, expected %s' % \
              (repr(s.pack(12345)), repr(_
