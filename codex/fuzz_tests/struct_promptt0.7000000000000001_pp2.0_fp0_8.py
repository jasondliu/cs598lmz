import _struct
# Test _struct.Struct.format_size()

def test_format_size():
    for code in 'bBhHiIlLfd':
        s = _struct.Struct(code)
        assert s.format_size() == _struct.calcsize(code)

def test_format_size_with_endian_char():
    for code in '@=<>!':
        for c in 'bBhHiIlLfd':
            s = _struct.Struct(code + c)
            assert s.format_size() == _struct.calcsize(code + c)

def test_format_size_with_explicit_repeat_count():
    for code in 'bBhHiIlLfd':
        s = _struct.Struct(2*code)
        assert s.format_size() == 2*_struct.calcsize(code)

def test_format_size_with_explicit_repeat_count_and_endian_char():
    for code in '@=<>!':
        for c in 'bBhHiIlLfd':
            s = _
