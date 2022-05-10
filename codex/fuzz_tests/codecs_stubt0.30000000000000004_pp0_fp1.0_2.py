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
    assert codecs.utf_16_encode("abc") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode("abc", "strict") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode("abc", "ignore") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode("abc", "replace") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode("abc", "xmlcharrefreplace") == (b'\xff\xfea\x00b\x00c\x00', 6)
    assert codecs.utf_16_encode("abc", "backslashreplace") == (b'\xff\xfe
