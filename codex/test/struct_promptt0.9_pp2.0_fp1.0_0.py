import _struct
# Test _struct.Struct with the '>' byteorder specifier.


def test_big_endian(tester):
    s = _struct.Struct(b'>i')
    values = (1, -1, 0, -256)
    for v in values:
        s.pack_into(tester.buffer, 0, v)
        tester.run_test()


def test_big_endian_packed(tester):
    s = _struct.Struct(b'>i')
    values = (1, -1, 0, -256)
    for v in values:
        s.pack(v)
        tester.run_test()


def test_big_endian_unpack(tester):
    s = _struct.Struct(b'>i')
    values = bytes(b'\x01\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00'
                    b'\x00\x00\xff\x00')
