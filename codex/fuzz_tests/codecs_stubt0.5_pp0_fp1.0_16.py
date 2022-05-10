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

def test_main():
    # UCS2
    try:
        codecs.decode("abc\x00\x00\x00d", "utf-16", "strict")
    except UnicodeDecodeError as exc:
        assert exc.object == b"abc\x00\x00\x00d"
        assert exc.end == 3
        assert exc.start == 3
        assert exc.reason == "truncated data"
        assert exc.encoding == "utf-16"
        assert str(exc) == "'utf-16' codec can't decode byte 0x0 in position 3: truncated data"
        assert repr(exc) == "UnicodeDecodeError('utf-16', b'abc\\x00\\x00\\x00d', 3, 4, 'truncated data')"
        assert exc.__cause__ is None
        assert exc.__context__ is None
    else:
        raise AssertionError("UnicodeDecodeError not raised")
    assert codecs.decode("abc\x00\x00\x00d", "
