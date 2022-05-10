import _struct
# Test _struct.Struct.format_size_ok()
for fmt in "bBhHiIlLqQfd":
    for endian in "<>=!":
        s = _struct.Struct(endian + fmt)
        s.format_size_ok()


def test_format_size_ok_overflow():
    # Format with size too large (overflow)
    import _struct
    s = _struct.Struct("@q")
    with pytest.raises(OverflowError):
        s.format_size_ok()

    # Format with size too large (overflow)
    import _struct
    s = _struct.Struct("@Q")
    with pytest.raises(OverflowError):
        s.format_size_ok()


def test_format_size_ok_bad_chars():
    # Bad character in format string
    import _struct
    s = _struct.Struct("@qxy")
    with pytest.raises(SystemError):
        s.format_size_ok()


