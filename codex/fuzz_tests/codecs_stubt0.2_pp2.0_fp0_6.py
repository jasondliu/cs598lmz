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
    # Test that the codecs module can be used to add a single codepoint
    # to a UnicodeDecodeError.
    try:
        "abc\xff".encode("ascii")
    except UnicodeEncodeError as exc:
        assert exc.object == "abc\xff"
        assert exc.start == 3
        assert exc.end == 4
        assert exc.reason == "ordinal not in range(128)"
        assert exc.encoding == "ascii"
        assert exc.args == ("ascii", "abc\xff", 3, 4, "ordinal not in range(128)")
        assert str(exc) == "'ascii' codec can't encode character '\\xff' in position 3: ordinal not in range(128)"
        assert exc.encode("ascii", "add_one_codepoint") == ("abc\xffa", 4)
        assert exc.encode("utf-16", "add_one_codepoint") == (b'abca\xff\xfe', 6)
        assert exc
