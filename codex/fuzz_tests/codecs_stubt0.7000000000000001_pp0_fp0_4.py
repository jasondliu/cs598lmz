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

def test_basic():
    assert "abc".encode("utf-8") == b'abc'
    assert b'abc'.decode("utf-8") == "abc"

    assert "abc".encode("utf-8", "strict") == b'abc'
    assert b'abc'.decode("utf-8", "strict") == "abc"

    raises(UnicodeDecodeError, b'\xff'.decode, "utf-8", "strict")
    raises(UnicodeDecodeError, "abc\ud800".encode, "utf-8", "strict")

def test_errors():
    import sys
    u = "abc\udc80"
    raises(UnicodeEncodeError, u.encode, "utf-8", "strict")

    u.encode("utf-8", "replace") == b'abc\ufffd'
    u.encode("utf-8", "ignore") == b'abc'
    u.encode("utf-8", "add_one_codepoint") == b'
