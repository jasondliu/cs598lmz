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
    # Testing UTF-8
    assert codecs.utf_8_decode(b"abc") == ("abc", 3)
    assert codecs.utf_8_decode(b"abc\xff") == ("abc\ufffd", 4)
    assert codecs.utf_8_decode(b"abc\xff", "replace") == ("abc\ufffd", 4)
    assert codecs.utf_8_decode(b"abc\xff", "ignore") == ("abc", 4)
    assert codecs.utf_8_decode(b"abc\xff", "backslashreplace") == ("abc\\xff", 4)
    assert codecs.utf_8_decode(b"abc\xff", "xmlcharrefreplace") == ("abc&#255;", 4)
    assert codecs.utf_8_decode(b"abc\xed\xa0\x80\xff", "replace") == ("abc\ufffd\ufffd\ufffd", 6)
    assert codecs.utf_8_decode(b"abc\
