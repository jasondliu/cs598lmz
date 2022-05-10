import _struct
# Test _struct.Struct for all code/value size combinations.
def test_all_format_c_values():
    fmt = _struct.Struct('')
    assert fmt.size == 0
    s = fmt.pack()
    assert len(s) == 0
    for code in 'xbBhHiIlLqQnNfdfdPp':
        for value in (-12345, 0, 12345):
            try:
                fmt = _struct.Struct(code)
            except OverflowError as msg:
                continue
            s = fmt.pack(value)
            assert len(s) == fmt.size
            try:
                res = fmt.unpack(s)
                assert res[0] == value
            except Exception:
                unknown_code(code, value)


def test_pack_into_buffer():
    buf = bytearray(20)
    fmt = _struct.Struct('I4s')
    fmt.pack_into(buf, 1, 12345, b'abcd')
    assert list(buf) == [0, 0x39, 0x30, 0x00
