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
    for encoding in ("utf-8", "UTF-8"):
        # Test encoding
        assert codecs.utf_8_encode("abc") == ("abc", 3)
        assert codecs.utf_8_encode("abc\u20ac") == ("abc\xe2\x82\xac", 7)
        assert codecs.utf_8_encode("\u20ac") == ("\xe2\x82\xac", 3)
        assert codecs.utf_8_encode("\U0001d120") == ("\xf0\x9d\x84\xa0", 4)
        assert codecs.utf_8_encode("\U0001d120\U0001d120") == ("\xf0\x9d\x84\xa0\xf0\x9d\x84\xa0", 8)
        assert codecs.utf_8_encode("\U0001d120\U0001d120", 'strict', True) == ("\xf0\x9d
