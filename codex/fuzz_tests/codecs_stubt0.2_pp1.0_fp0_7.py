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
    assert codecs.utf_8_decode(b'\xff') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\xff', errors='ignore') == ('', 1)
    assert codecs.utf_8_decode(b'\xff', errors='replace') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\xff', errors='add_one_codepoint') == ('a', 1)
    assert codecs.utf_8_decode(b'\xff', errors='add_utf16_bytes') == ('a', 1)
    assert codecs.utf_8_decode(b'\xff', errors='add_utf32_bytes') == ('a', 1)
    assert codecs.utf_8_decode(b'\xff', errors='strict') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\xff', errors='surrogateescape') == ('
