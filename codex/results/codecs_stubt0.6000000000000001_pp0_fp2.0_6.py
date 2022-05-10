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

def test_utf8_decode():
    assert b"abc\xff".decode("utf-8") == "\uFFFDabc\uFFFD"
    assert b"abc\xff".decode("utf-8", "ignore") == "abc"
    assert b"abc\xff".decode("utf-8", "replace") == "abc\ufffd"
    assert b"\xff".decode("utf-8", "add_one_codepoint") == "a\uFFFD"

def test_utf8_encode():
    assert "\uFFFDabc\uFFFD".encode("utf-8") == b"abc\xff"
    assert "\uFFFDabc\uFFFD".encode("utf-8", "ignore") == b"abc"
    assert "\uFFFDabc\uFFFD".encode("utf-8", "replace") == b"abc\xff"
    assert "\uFFFD".encode("utf-8", "add_one_codepoint") == b"a\xff"

def test_utf16_dec
