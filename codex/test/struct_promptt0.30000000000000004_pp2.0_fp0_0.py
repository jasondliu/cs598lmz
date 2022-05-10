import _struct
# Test _struct.Struct

def test_struct_pack_unpack():
    # Test packing and unpacking of all native types.
    # Also test byte order, size, and alignment,
    # using the 'x' format.
    import sys
    import _struct
    for code in 'bBhHiIlLqQfd':
        fmt = '=' + code
        size = _struct.calcsize(fmt)
        x = (code * size).encode('latin-1')
        s = _struct.Struct(fmt)
        got = s.unpack(s.pack(x))
        assert got == (x,)
        assert s.size == size
        assert s.pack_into(x, 0, x) is None
        assert s.unpack_from(x, 0) == (x,)
        if sys.byteorder == 'little':
            fmt = '<' + code
        else:
            fmt = '>' + code
        size = _struct.calcsize(fmt)
        x = (code * size).encode('latin-1')
       
