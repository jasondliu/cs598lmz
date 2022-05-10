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

def test_unicode_decode_error():
    # Test UnicodeDecodeError
    try:
        b"abc\xff".decode("ascii")
    except UnicodeDecodeError as exc:
        assert exc.object == b"abc\xff"
        assert exc.encoding == "ascii"
        assert exc.start == 3
        assert exc.end == 4
        assert exc.reason == "ordinal not in range(128)"
        assert str(exc) == "'ascii' codec can't decode byte 0xff in position 3: ordinal not in range(128)"
        assert exc.__reduce__() == (UnicodeDecodeError,
            (b"abc\xff", "ascii", 3, 4, "ordinal not in range(128)"))
    else:
        assert False, "UnicodeDecodeError not raised"
    assert b"abc\xff".decode("ascii", "ignore") == "abc"
    assert b"abc\xff".decode("ascii", "replace") == "abc?"
    assert
