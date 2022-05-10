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

# Test UnicodeEncodeError

def test_unicodeencode():
    assert u"\u0100".encode("ascii", "add_one_codepoint") == b"a"
    assert u"\u0100".encode("utf-16", "add_utf16_bytes") == b"ab"
    assert u"\u0100".encode("utf-32", "add_utf32_bytes") == b"abcd"

# Test UnicodeDecodeError

def test_unicodedecode():
    assert b"\x80".decode("ascii", "add_one_codepoint") == "a"
    assert b"\x80".decode("utf-16", "add_utf16_bytes") == "ab"
    assert b"\x80".decode("utf-32", "add_utf32_bytes") == "abcd"

# Test UnicodeTranslateError

def test_unicodetranslate():
    assert u"\u0100".translate({0x100: u"a"}) == "a"
