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
    # Test the UTF-8 codec
    for encoding in ("utf-8", "utf_8"):
        # Test decoding
        assert codecs.utf_8_decode(b"abc") == ("abc", 3)
        assert codecs.utf_8_decode(b"abc\xff") == ("abc\ufffd", 4)
        assert codecs.utf_8_decode(b"abc\xff", "replace") == ("abc\ufffd", 4)
        assert codecs.utf_8_decode(b"abc\xff", "ignore") == ("abc", 4)
        assert codecs.utf_8_decode(b"abc\xff", "strict") == ("abc\ufffd", 4)
        assert codecs.utf_8_decode(b"abc\xff", "add_one_codepoint") == ("abca", 4)
        assert codecs.utf_8_decode(b"abc\xff", "add_utf16_bytes") == ("abca", 4)
        assert codecs.utf
