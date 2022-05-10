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
    assert codecs.utf_8_decode(b'\xc3\xa9', "replace") == ('\u00e9', 2)
    assert codecs.utf_8_decode(b'\xc3', "replace") == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\xc3', "ignore") == ('', 1)
    assert codecs.utf_8_decode(b'\xc3', "add_one_codepoint") == ('\u00e9', 1)
    assert codecs.utf_8_decode(b'\xc3', "add_utf16_bytes") == ('\u00e9', 2)
    assert codecs.utf_8_decode(b'\xc3', "add_utf32_bytes") == ('\u00e9', 4)
    assert codecs.utf_8_decode(b'\xc3', "strict", True) == ('\u00e9', 1)
   
