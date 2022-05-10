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
    # test UnicodeEncodeError
    try:
        u'\udc80'.encode("ascii")
    except UnicodeEncodeError as exc:
        assert exc.encoding == "ascii"
        assert exc.object == u'\udc80'
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "surrogates not allowed"
        assert str(exc) == "'ascii' codec can't encode character '\\udc80' in position 0: surrogates not allowed"

    # test UnicodeDecodeError
    try:
        b'\x80'.decode("ascii")
    except UnicodeDecodeError as exc:
        assert exc.encoding == "ascii"
        assert exc.object == b'\x80'
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "ordinal not in range(128)"
        assert str(exc) == "'ascii' codec can't decode byte 0x80 in position 0:
