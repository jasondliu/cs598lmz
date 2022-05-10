import _struct
# Test _struct.Struct class for all packaging types with all combinations of
# native/standard/big/little byte orders.

def test_struct():
    for p in all_struct_types:
        big_endian_p = p[0].upper() + p[1:]
        for c in '@=<>!':
            for big_endian in (True, False):
                if big_endian:
                    endian_str = '>'
                else:
                    endian_str = '<'
                s = _struct.Struct(c+p)
                packed = s.pack(1, 'abc', 2)
                unpacked = s.unpack(packed)
                assert unpacked == (1, b'abc', 2)
                s = _struct.Struct(c+big_endian_p)
                packed = s.pack(1, 'abc', 2)
                unpacked = s.unpack(packed)
                assert unpacked == (1, b'abc', 2)
                s = _struct.Struct(endian_str+p)
                packed = s.pack(1
