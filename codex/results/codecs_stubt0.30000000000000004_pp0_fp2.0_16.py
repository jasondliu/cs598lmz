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
    # test utf-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        assert codecs.decode(b"\xff", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe\x00", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe\x00\x00", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe\x00\x00\x00", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe\x00\x00\x00\x00", enc, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe\x00\x00\x00\
