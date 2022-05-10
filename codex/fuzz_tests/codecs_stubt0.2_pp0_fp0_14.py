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
    # Test UnicodeEncodeError
    try:
        u"\u1234".encode("ascii", "add_one_codepoint")
    except UnicodeEncodeError as exc:
        assert exc.object == u"\u1234"
        assert exc.encoding == "ascii"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "add_one_codepoint"
        assert str(exc) == " 'ascii' codec can't encode character '\\u1234' in position 0: add_one_codepoint"
    else:
        raise AssertionError("UnicodeEncodeError not raised")

    # Test UnicodeDecodeError
    try:
        b"\xff".decode("ascii", "add_one_codepoint")
    except UnicodeDecodeError as exc:
        assert exc.object == b"\xff"
        assert exc.encoding == "ascii"
        assert exc.start == 0
        assert exc.end
