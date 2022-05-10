import _struct
# Test _struct.Struct

import _struct

def test_struct(fmt, expected, *args):
    s = _struct.Struct(fmt)
    got = s.pack(*args)
    assert len(got) == s.size, 'packed string wrong size'
    assert got == expected, 'pack returns wrong value'
    assert s.unpack(got) == args, 'unpack returns wrong value'
    assert s.unpack_from(buffer(got)) == args, 'unpack_from returns wrong value'

def test_struct_error(fmt, *args):
    s = _struct.Struct(fmt)
    try:
        s.pack(*args)
    except _struct.error:
        pass
    else:
        assert False, 'expected error'

def test_struct_unpack_error(fmt, data):
    s = _struct.Struct(fmt)
    try:
        s.unpack(data)
    except _struct.error:
        pass
    else:
        assert False, 'expected error'

