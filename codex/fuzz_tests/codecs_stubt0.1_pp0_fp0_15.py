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
    for encoding in ("utf-16", "utf-16-be", "utf-16-le"):
        # Test decoding
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding) == '\x00'
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding, "replace") == '\ufffd'
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding, "ignore") == ''
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding, "add_one_codepoint") == 'a\x00'
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding, "add_utf16_bytes") == 'ab\x00'
        assert codecs.decode(b'\xff\xfe\x00\x00', encoding, "add_utf32_bytes") == '
