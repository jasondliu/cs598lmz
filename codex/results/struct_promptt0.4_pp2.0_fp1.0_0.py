import _struct
# Test _struct.Struct

def test_struct_error():
    # Check invalid format strings
    for fmt in ['@', '=', '<', '>', '!', 'x', 'X']:
        try:
            s = _struct.Struct(fmt)
        except ValueError:
            pass
        else:
            print('expected ValueError for format %r' % fmt)

    # Check invalid format strings for unpack
    for fmt in ['@', '=', '<', '>', '!', 'x', 'X', 'c', 's', 'p', 'P']:
        try:
            s = _struct.Struct(fmt)
            s.unpack(b'')
        except ValueError:
            pass
        else:
            print('expected ValueError for format %r' % fmt)

    # Check invalid format strings for unpack_from
    for fmt in ['@', '=', '<', '>', '!', 'x', 'X', 'c', 's', 'p', 'P']:
        try:
            s = _struct.Struct(fmt
