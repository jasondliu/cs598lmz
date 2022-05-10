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

# Test UTF-8

def test_utf8_decode(encoding):
    # Test decoding with errors
    assert codecs.utf_8_decode(b'\xff', "strict") == (0xfffd, 1)
    assert codecs.utf_8_decode(b'\xff', "replace") == (0xfffd, 1)
    assert codecs.utf_8_decode(b'\xff', "ignore") == (0, 1)
    assert codecs.utf_8_decode(b'\xff', "backslashreplace") == (0x5cff, 1)
    assert codecs.utf_8_decode(b'\xff', "xmlcharrefreplace") == (0x26ff, 1)
    assert codecs.utf_8_decode(b'\xff', "add_one_codepoint") == ('a', 1)
    assert codecs.utf_8_decode(b'\xff', "add_utf16_bytes") == (0xfffd, 1)
    assert codecs.utf
