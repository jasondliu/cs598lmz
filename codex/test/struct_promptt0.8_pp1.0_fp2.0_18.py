import _struct
# Test _struct.Struct
def test_struct():
    data = b'\x00\x0c\x12\x34hello'
    unpack_test_list = (
        ('!H', ((0x0c,),)),
        ('i', ((0x1234,),)),
        ('6s', ((b'hello',),)),
        ('Hi', ((0x0c, 0x1234),)),
        ('i6s', ((0x1234, b'hello'),)),
        ('!Hi6s', ((0x0c, 0x1234, b'hello'),)),
        )
    for fmt, value in unpack_test_list:
        s = _struct.Struct(fmt)
        d = s.unpack_from(data)
        eq_(d, value)
        s = _struct.Struct(fmt)
        d = s.unpack(data)
        eq_(d, value)
