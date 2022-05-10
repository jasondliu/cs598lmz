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
    # Test UTF-16-BE
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x00', "replace") == ('\u0000', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x00', "ignore") == ('', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x00', "add_one_codepoint") == ('a\u0000', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x00', "add_utf16_bytes") == ('a\u0000', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x00', "add_utf32_bytes") == ('a\u0000', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\
