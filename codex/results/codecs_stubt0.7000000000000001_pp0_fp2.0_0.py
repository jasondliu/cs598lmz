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

# Two-byte encoding tests

def test_utf_16_be_handler():
    t = codecs.getdecoder('utf-16-be')
    assert t(b'\xff\xfe\x00\x61\x00\x62', "add_one_codepoint") == ('a\x00', 4)
    assert t(b'\xff\xfe\x00\x61\x00\x62', "add_utf16_bytes") == ('a\x00', 4)
    assert t(b'\xff\xfe\x00\x61\x00\x62', "add_utf32_bytes") == ('a\u0000\u0000\u0000', 4)

    assert t(b'\x00\x61\x00\x62', "add_one_codepoint") == ('a\x00', 4)
    assert t(b'\x00\x61\x00\x62', "add_utf16_bytes") == ('a\x00', 4)
    assert t(b'\x
