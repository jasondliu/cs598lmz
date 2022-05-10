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
    u = bytes(range(0x100))
    try:
        u.decode("ascii", "strict")
    except UnicodeDecodeError as exc:
        assert exc.object is u
        assert exc.encoding == "ascii"
        assert exc.start == 128
        assert exc.end == 256
        assert exc.reason == "ordinal not in range(128)"
        assert str(exc) == ("'ascii' codec can't decode byte 0x80 in position 128: "
                            "ordinal not in range(128)")
        assert exc.object[exc.start:exc.end] == b"\x80"
        assert exc.args == ("ascii", b"\x80", 128, 129, "ordinal not in range(128)")
        assert exc.__cause__ is None
        assert exc.__context__ is None
        assert exc.__suppress_context__ is False
        assert exc.with_traceback(None) is
