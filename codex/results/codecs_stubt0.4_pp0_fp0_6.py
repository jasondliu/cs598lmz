import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_utf16_exception(encoding):
    # Test that the error handler is called with the correct number of bytes
    # when the input contains a partial code unit.

    # The UTF-16LE and UTF-16BE codecs should call the error handler with
    # two bytes.
    if encoding in ("utf-16-le", "utf-16-be"):
        expected = b'ab'
    # The UTF-16 codec should call the error handler with four bytes.
    else:
        expected = b'abcd'

    # The input contains a partial code unit.
    s = b'\xff\xff\xff'
    with pytest.raises(UnicodeDecodeError) as excinfo:
        s.decode(encoding)
    assert excinfo.value.object == s
    assert excinfo.value.start == 0
    assert excinfo.value.end == 2
    assert excinfo.value.reason == "truncated data"
    assert excinfo.value.encoding == encoding
    assert excinfo.value.args == (s,
