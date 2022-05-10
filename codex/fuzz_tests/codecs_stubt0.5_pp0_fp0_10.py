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
    # Test encoding
    assert "abc".encode("ascii", "add_one_codepoint") == b'abc'
    assert "abc".encode("ascii", "add_utf16_bytes") == b'abc'
    assert "abc".encode("ascii", "add_utf32_bytes") == b'abc'
    assert "abc".encode("utf-8", "add_one_codepoint") == b'abc\xc3\xa1'
    assert "abc".encode("utf-8", "add_utf16_bytes") == b'abc\x00\x61'
    assert "abc".encode("utf-8", "add_utf32_bytes") == b'abc\x00\x00\x00\x61'
    assert "abc".encode("utf-16", "add_one_codepoint") == b'abc\x00\x61'
    assert "abc".encode("utf-16", "add_utf16_bytes") == b'abc\x00
