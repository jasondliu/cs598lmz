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
        u"\u0100".encode("ascii")
    except UnicodeEncodeError as exc:
        assert str(exc) == "'ascii' codec can't encode character '\\u0100' in position 0: ordinal not in range(128)", str(exc)
        assert exc.object == u"\u0100"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "ordinal not in range(128)"
        assert exc.encoding == "ascii"
        assert exc.args == (u"\u0100", 0, 1, "ordinal not in range(128)", "ascii")
        assert exc.__reduce__() == (UnicodeEncodeError, (u"\u0100", 0, 1, "ordinal not in range(128)", "ascii"))

        # Test with a custom __str__
        class Exc(UnicodeEncodeError):
            def __str__(self):
                return "test"

