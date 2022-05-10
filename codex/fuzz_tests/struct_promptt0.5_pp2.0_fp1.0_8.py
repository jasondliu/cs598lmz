import _struct
# Test _struct.Struct

# Test internal methods

def test_internal():
    # check __doc__ for every method
    for name in dir(_struct.Struct):
        if name[:1] == '_': continue
        obj = getattr(_struct.Struct, name)
        if hasattr(obj, '__doc__'):
            assert obj.__doc__, '%s has empty or missing docstring' % name

def test_sizeof():
    # Test that we can get the size of a struct without packing it
    s = _struct.Struct('hi')
    assert s.size == 4

def test_pack_error():
    # Too many arguments
    s = _struct.Struct('i')
    try:
        s.pack(1, 2)
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'
    # Too few arguments
    try:
        s.pack()
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'
    # Wrong argument type
    try:
        s.pack('
