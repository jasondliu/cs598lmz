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

def test_utf8_decode(encoding):
    # Test UTF-8 decoding
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "strict", True) == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "strict", False) == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "replace", True) == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "replace", False) == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "ignore", True) == ('\n', 0)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "ignore", False) == ('\n', 0)
    assert
