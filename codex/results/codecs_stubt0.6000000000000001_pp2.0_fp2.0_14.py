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

def test_utf8():
    # test UTF-8
    u8 = "abc\xe2\x82\xac\xff".encode("utf-8")
    assert u8.decode("utf-8", "strict") == "abc\u20ac\ufffd"
    assert u8.decode("utf-8", "replace") == "abc\u20ac\ufffd"
    assert u8.decode("utf-8", "ignore") == "abc"
    assert u8.decode("utf-8", "add_one_codepoint") == "abca\ufffd"
    assert u8.decode("utf-8", "add_utf16_bytes") == "abca\ufffd"
    assert u8.decode("utf-8", "add_utf32_bytes") == "abca\ufffd"
    raises(UnicodeDecodeError, u8.decode, "utf-8", "backslashreplace")
    raises(UnicodeDecodeError, u8.decode, "utf-8", "
