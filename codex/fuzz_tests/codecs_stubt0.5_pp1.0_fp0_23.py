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

def test_utf32_be_decode():
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "strict") == ('', 0)
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "replace") == ('\ufffd', 0)
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "ignore") == ('', 0)
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "add_one_codepoint") == ('a', 0)
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "add_utf16_bytes") == ('a', 0)
    assert codecs.utf_32_be_decode(b'\0\0\0\0', "add_utf32_bytes") == ('a', 0)
    assert codecs.utf_32_be_decode(
