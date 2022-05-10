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

def test_unicode_encode_error():
    # Test UnicodeEncodeError
    u = "\ud800"
    try:
        u.encode("ascii")
    except UnicodeEncodeError as exc:
        assert exc.object == u
        assert exc.encoding == "ascii"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "surrogates not allowed"
        assert str(exc) == " 'ascii' codec can't encode character '\\ud800' in position 0: surrogates not allowed"

    try:
        u.encode("ascii", "replace")
    except UnicodeEncodeError as exc:
        assert exc.object == u
        assert exc.encoding == "ascii"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "surrogates not allowed"
        assert str(exc) == " 'ascii' codec can't encode character '\\ud800' in position 0: surrogates not allowed"

    try:

