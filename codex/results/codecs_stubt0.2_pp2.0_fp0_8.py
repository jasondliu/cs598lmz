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

# Test the UTF-16 codec

def test_utf16_encode(encoding):
    assert codecs.utf_16_encode(u"abc") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode(u"abc", "strict") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode(u"abc", "ignore") == (b'', 0)
    assert codecs.utf_16_encode(u"abc", "replace") == (b'\xff\xfea\x00b\x00?\x00', 6)
    assert codecs.utf_16_encode(u"abc", "xmlcharrefreplace") == (b'&#97;&#98;&#99;', 12)
    assert codecs.utf_16_encode(u"abc", "backslashreplace") == (b'\\u0061\\u
