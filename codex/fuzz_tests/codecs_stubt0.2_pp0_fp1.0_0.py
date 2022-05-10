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
    # Test UTF-16
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        # Test decoding
        assert codecs.decode("\xff\xfe\x00\x00", encoding, "add_one_codepoint") == "\x00\x00"
        assert codecs.decode("\xff\xfe\x00\x00", encoding, "add_utf16_bytes") == "\x00\x00"
        assert codecs.decode("\xff\xfe\x00\x00", encoding, "add_utf32_bytes") == "\x00\x00"
        # Test encoding
        assert codecs.encode("\x00\x00", encoding, "add_one_codepoint") == "\xff\xfe\x00\x00"
        assert codecs.encode("\x00\x00", encoding, "add_utf16_bytes") == "\xff\xfe\x00\x00"
        assert codecs.encode("
