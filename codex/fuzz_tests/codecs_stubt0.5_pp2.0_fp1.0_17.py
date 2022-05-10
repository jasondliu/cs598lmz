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
    # Test encoding
    assert codecs.utf_16_encode(u"\u20ac") == (b'\xac\u20', 2)
    assert codecs.utf_16_encode(u"\u20ac", "strict") == (b'\xac\u20', 2)
    assert codecs.utf_16_encode(u"\u20ac", "replace") == (b'\xac\u20', 2)
    assert codecs.utf_16_encode(u"\u20ac", "ignore") == (b'', 0)
    assert codecs.utf_16_encode(u"\u20ac", "add_one_codepoint") == (b'a\xac\u20', 2)
    assert codecs.utf_16_encode(u"\u20ac", "add_utf16_bytes") == (b'ab\xac\u20', 2)
    assert codecs.utf_16_encode(u"\u20ac", "add
