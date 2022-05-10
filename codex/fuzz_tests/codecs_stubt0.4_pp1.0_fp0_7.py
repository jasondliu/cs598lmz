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
    assert codecs.utf_8_decode("\xff") == ("\ufffd", 1)
    assert codecs.utf_8_decode("\xff", "replace") == ("\ufffd", 1)
    assert codecs.utf_8_decode("\xff", "ignore") == ("", 1)
    assert codecs.utf_8_decode("\xff", "add_one_codepoint") == ("a", 1)

    assert codecs.utf_8_decode("\xff\xff") == ("\ufffd\ufffd", 2)
    assert codecs.utf_8_decode("\xff\xff", "replace") == ("\ufffd\ufffd", 2)
    assert codecs.utf_8_decode("\xff\xff", "ignore") == ("", 2)
    assert codecs.utf_8_decode("\xff\xff", "add_one_codepoint") == ("a", 2)

    assert codecs.utf_8_decode("\xff
