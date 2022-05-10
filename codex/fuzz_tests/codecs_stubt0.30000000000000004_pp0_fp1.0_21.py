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
    # Test UTF-8
    for encoding in ("utf_8", "utf-8"):
        # Test decoding
        assert codecs.decode("\x80", encoding) == "\ufffd"
        assert codecs.decode("\x80", encoding, "replace") == "\ufffd"
        assert codecs.decode("\x80", encoding, "ignore") == ""
        assert codecs.decode("\x80", encoding, "add_one_codepoint") == "a"
        assert codecs.decode("\x80", encoding, "add_utf16_bytes") == "\ufffdab"
        assert codecs.decode("\x80", encoding, "add_utf32_bytes") == "\ufffdabcd"
        # Test encoding
        assert codecs.encode("\udc80", encoding) == "\xed\xb2\x80"
        assert codecs.encode("\udc80", encoding, "replace") == "\xef\xbf\xbd"
        assert codecs.encode
