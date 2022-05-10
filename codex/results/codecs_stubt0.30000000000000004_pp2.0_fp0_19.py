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

# test utf-16-le

def test_utf16_le(encoding):
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00', "replace") == ('\x00', 2)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00', "ignore") == ('', 2)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00', "xmlcharrefreplace") == ('&#x0;', 2)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00', "backslashreplace") == ('\\x00', 2)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00', "namereplace") == ('\\N{NULL}', 2)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x
