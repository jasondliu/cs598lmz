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

def test_utf8(input, expected):
    assert codecs.decode(input, "utf-8", "strict") == expected
    assert codecs.decode(input, "utf-8", "replace") == expected
    assert codecs.decode(input, "utf-8", "ignore") == expected
    assert codecs.decode(input, "utf-8", "add_one_codepoint") == expected
    assert codecs.decode(input, "utf-8", "add_utf16_bytes") == expected
    assert codecs.decode(input, "utf-8", "add_utf32_bytes") == expected

def test_utf16(input, expected):
    assert codecs.decode(input, "utf-16", "strict") == expected
    assert codecs.decode(input, "utf-16", "replace") == expected
    assert codecs.decode(input, "utf-16", "ignore") == expected
    assert codecs.decode(input, "utf-16", "add_one_codepoint
