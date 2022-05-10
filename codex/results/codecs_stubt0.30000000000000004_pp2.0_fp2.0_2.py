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
    # test utf-8 decoding
    assert encoding.utf_8_decode(b'abc') == ('abc', 3)
    assert encoding.utf_8_decode(b'\xc3\xa9') == ('\xe9', 2)
    assert encoding.utf_8_decode(b'\xc3\xa9', errors='strict') == ('\xe9', 2)
    assert encoding.utf_8_decode(b'\xc3\xa9', errors='replace') == ('\xe9', 2)
    assert encoding.utf_8_decode(b'\xc3\xa9', errors='ignore') == ('', 2)
    assert encoding.utf_8_decode(b'\xc3\xa9', errors='add_one_codepoint') == ('a\xe9', 2)
    assert encoding.utf_8_decode(b'\xc3\xa9', errors='add_utf16_bytes') == ('a\xe9', 2)
    assert encoding.
