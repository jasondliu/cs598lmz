import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, 'expected TypeError'

def test_struct_unpack():
    s = _struct.Struct('i')
    d = s.unpack(s.pack(12345))
    if d != (12345,):
        raise TestFailed, 'expected (12345,), got %r' % (d,)

def test_struct_unpack_bigendian():
    s = _struct.Struct('>i')
    d = s.unpack(s.pack(12345))
    if d != (12345,):
        raise TestFailed, 'expected (12345,), got %r' % (d,)

def test_struct_unpack_littleendian():
    s = _struct.Struct('<i')
    d = s.unpack(s.pack(12345))
    if d != (12345,):
        raise TestFailed, 'expected (12345,),
