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
    # Test utf-16-le
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00\x00\x00\x00\x00', "replace") == ('\U00000000', 6)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00\x00\x00\x00\x00', "ignore") == ('', 6)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00\x00\x00\x00\x00', "add_one_codepoint") == ('a\U00000000', 6)
    assert codecs.utf_16_le_decode(b'\xff\xfe\x00\x00\x00\x00\x00\x00', "add_utf16_bytes") == ('ab\U00000000', 6)
    assert codecs.utf_16_le_decode(b'\xff\
