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

def test_utf8_decode_errors():
    # test utf-8 decoding with errors
    for i in range(0, 128):
        assert codecs.utf_8_decode(bytes([i]), "strict") == (chr(i), 1)

    assert codecs.utf_8_decode(b'\xc0', "strict") == ("\ufffd", 1)
    assert codecs.utf_8_decode(b'\xc0', "ignore") == ("", 1)
    assert codecs.utf_8_decode(b'\xc0', "replace") == ("\ufffd", 1)
    assert codecs.utf_8_decode(b'\xc0', "add_one_codepoint") == ("a", 1)
    assert codecs.utf_8_decode(b'\xc0', "add_utf16_bytes") == ("a", 1)
    assert codecs.utf_8_decode(b'\xc0', "add_utf32_bytes") == ("a", 1)

   
