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
    assert codecs.utf_8_decode(b'\xff') == (u'\ufffd', 1)
    assert codecs.utf_8_decode(b'\xff', "replace") == (u'\ufffd', 1)
    assert codecs.utf_8_decode(b'\xff', "ignore") == (u'', 1)
    assert codecs.utf_8_decode(b'\xff', "add_one_codepoint") == (u'a', 1)
    assert codecs.utf_8_decode(b'\xff', "add_utf16_bytes") == (u'ab', 1)
    assert codecs.utf_8_decode(b'\xff', "add_utf32_bytes") == (u'abcd', 1)
    assert codecs.utf_8_decode(b'\xff', "strict", True) == (u'\ufffd', 1)
    assert codecs.utf_8_decode(b'\
