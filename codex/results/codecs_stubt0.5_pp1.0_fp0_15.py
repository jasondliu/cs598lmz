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

def test_encode():
    assert codecs.utf_16_encode(b'ab', "add_one_codepoint") == (b'\xff\xfea\x00b', 2)
    assert codecs.utf_16_encode(b'ab', "add_utf16_bytes") == (b'\xff\xfea\x00b\x00', 2)

    assert codecs.utf_32_encode(b'ab', "add_one_codepoint") == (b'\xff\xfe\x00\x00a\x00\x00\x00', 2)
    assert codecs.utf_32_encode(b'ab', "add_utf32_bytes") == (b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00', 2)

def test_decode():
    assert codecs.utf_16_decode(b'\xff\xfea\x00b', "add_one_codepoint
