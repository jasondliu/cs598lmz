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
    assert codecs.utf_8_decode(b'\xc0\x80') == ('\ufffd\ufffd', 2)
    assert codecs.utf_8_decode(b'\xc0\x80', "replace") == ('\ufffd\ufffd', 2)
    assert codecs.utf_8_decode(b'\xc0\x80', "ignore") == ('', 2)
    assert codecs.utf_8_decode(b'\xc0\x80', "add_one_codepoint") == ('a\ufffd', 2)
    assert codecs.utf_8_decode(b'\xc0\x80', "add_utf16_bytes") == ('\ufffd\ufffd', 2)
    assert codecs.utf_8_decode(b'\xc0\x80', "add_utf32_bytes") == ('\uff
