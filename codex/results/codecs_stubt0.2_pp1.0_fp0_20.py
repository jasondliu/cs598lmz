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
    assert codecs.utf_8_decode(b'\x80', "strict") == (u'\uFFFD', 1)
    assert codecs.utf_8_decode(b'\x80', "replace") == (u'\ufffd', 1)
    assert codecs.utf_8_decode(b'\x80', "ignore") == (u'', 1)
    assert codecs.utf_8_decode(b'\x80', "add_one_codepoint") == (u'a', 1)
    assert codecs.utf_8_decode(b'\x80', "add_utf16_bytes") == (u'a', 1)
    assert codecs.utf_8_decode(b'\x80', "add_utf32_bytes") == (u'a', 1)
    assert codecs.utf_8_decode(b'\x80', "backslashreplace") == (u'\\x80', 1)
    assert codecs
