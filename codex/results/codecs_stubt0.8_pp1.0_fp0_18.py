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

def check_byte_decode(encoding, s, replacements, expected):
    assert codecs.decode(bytes(s, encoding), encoding, "replace") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "ignore") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "backslashreplace") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "xmlcharrefreplace") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "add_one_codepoint") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "add_utf16_bytes") == expected
    assert codecs.decode(bytes(s, encoding), encoding, "add_utf32_bytes") == expected

def check_unicode_encode(encoding, s, replacements, expected):
    assert codecs.encode(s, encoding, "replace") == expected
    assert codecs.encode(s, encoding, "ignore") == expected
    assert codec
