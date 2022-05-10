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
    assert codecs.utf_8_decode(b'\x80') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\x80', errors='strict') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\x80', errors='replace') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\x80', errors='ignore') == ('', 1)
    assert codecs.utf_8_decode(b'\x80', errors='add_one_codepoint') == ('a', 1)
    assert codecs.utf_8_decode(b'\x80', errors='add_utf16_bytes') == ('a', 1)
    assert codecs.utf_8_decode(b'\x80', errors='add_utf32_bytes') == ('a', 1)

    # Test UTF-16
    assert codecs.utf_16_decode(
