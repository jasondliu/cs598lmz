import _struct
# Test _struct.Struct()

def test():
    def _test_format(fmt, expected_size, expected_alignment):
        s = _struct.Struct(fmt)
        assert s.size == expected_size
        assert s.alignment == expected_alignment
        assert s.format == fmt
    _test_format('b', 1, 1)
    _test_format('i', 4, 4)
    _test_format('l', 4, 4)
    _test_format('n', 2, 2)
    _test_format('q', 8, 8)
    _test_format('B', 1, 1)
    _test_format('I', 4, 4)
    _test_format('L', 4, 4)
    _test_format('N', 4, 4)
    _test_format('Q', 8, 8)
    _test_format('f', 4, 4)
    _test_format('d', 8, 8)
    _test_format('s', 1, 1)
    _test_format('p', 4, 4)

    # nested
   
