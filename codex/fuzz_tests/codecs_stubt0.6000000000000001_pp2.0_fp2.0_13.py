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

def test_errors():
    # encoding
    assert codecs.charmap_encode("abc\xff\u0100") == (b"abc\xff\xfd\xbd", 2)
    assert codecs.charmap_encode("abc\xff\u0100", "strict") == (b"abc\xff\xfd\xbd", 2)
    assert codecs.charmap_encode("abc\xff\u0100", "replace") == (b"abc\xff?", 2)
    assert codecs.charmap_encode("abc\xff\u0100", "ignore") == (b"abc\xff", 2)

    assert codecs.charmap_encode("abc\xff\u0100", "strict",
                                 {"\xff": None, "\u0100": 0x100}) == (b"abc\x00\x01", 2)
    assert codecs.charmap_encode("abc\xff\u0100", "replace",
                                 {"\xff": None, "\u0100": 0x100}) == (b"abc\x
