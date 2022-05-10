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
    for encoding in ("ascii", "latin-1", "utf-8", "utf-16", "utf-32"):
        try:
            u"\u1234".encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.encoding == encoding
            assert exc.object == u"\u1234"
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "illegal encoding"
            assert str(exc) == "'%s' codec can't encode character '\\u1234' in position 0: %s" % (encoding, exc.reason)
            assert exc.encode("ascii", "backslashreplace") == "\\u1234".encode("ascii", "backslashreplace")
            assert exc.encode("ascii", "ignore") == b""
            assert exc.encode("ascii", "replace") == b"??"
            assert exc.encode("ascii", "xmlchar
