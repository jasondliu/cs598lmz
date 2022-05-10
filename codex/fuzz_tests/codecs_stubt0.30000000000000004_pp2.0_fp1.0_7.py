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
    assert codecs.decode(input, "utf-8", "add_one_codepoint") == expected

def test_utf16(input, expected):
    assert codecs.decode(input, "utf-16", "add_utf16_bytes") == expected

def test_utf32(input, expected):
    assert codecs.decode(input, "utf-32", "add_utf32_bytes") == expected

def test_utf8_surrogateescape(input, expected):
    assert codecs.decode(input, "utf-8", "surrogateescape") == expected

def test_utf16_surrogateescape(input, expected):
    assert codecs.decode(input, "utf-16", "surrogateescape") == expected

def test_utf32_surrogateescape(input, expected):
    assert codecs.decode(input, "utf-32", "surrogateescape") == expected

def test_utf8_surrogatepass(input, expected):
