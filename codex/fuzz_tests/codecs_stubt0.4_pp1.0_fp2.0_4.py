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
    # Testing UTF-16
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x00', "replace") == (u'\ufffd', 4)
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x00', "ignore") == (u'', 4)
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x00', "add_one_codepoint") == (u'\ufffd\ufffd', 4)
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x00', "add_utf16_bytes") == (u'\ufffd\ufffd', 4)
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x00', "add_utf32_bytes") == (u'\ufffd\ufffd', 4)

    # Testing UTF-32
    assert codecs.utf_32_decode
