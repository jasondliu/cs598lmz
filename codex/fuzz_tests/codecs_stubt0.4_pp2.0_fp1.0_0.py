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

def test_utf16_decode_errors():
    # Test UTF-16 decoding errors
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        # With a surrogate
        s = b'\x00\xd8'
        assert codecs.decode(s, encoding, "add_one_codepoint") == '\ud800'
        assert codecs.decode(s, encoding, "add_utf16_bytes") == '\ud800a'
        assert codecs.decode(s, encoding, "add_utf32_bytes") == '\ud800abcd'
        # Without a surrogate
        s = b'\x00\xd8'
        assert codecs.decode(s, encoding, "add_one_codepoint") == '\ud800'
        assert codecs.decode(s, encoding, "add_utf16_bytes") == '\ud800a'
        assert codecs.decode(s, encoding, "add_utf32_bytes") == '\ud800abcd'
