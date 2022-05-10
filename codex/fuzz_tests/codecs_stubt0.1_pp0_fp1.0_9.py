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
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "strict") == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "replace") == ('\xe9\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "ignore") == ('\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "backslashreplace") == ('\\xe9\\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "xmlcharrefreplace") == ('&#xe9;\n', 2)
    assert codecs.utf_8_decode(b'\xc3\xa9\n', "add_one_codepoint") == ('\xe9a\n', 3
