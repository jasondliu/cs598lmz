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

def test_issue3304():
    assert u"\ufffd".encode("utf-16be", "add_one_codepoint") == b"\x00a"
    assert u"\ufffd".encode("utf-32be", "add_one_codepoint") == b"\x00\x00\x00a"
    raises(UnicodeDecodeError, u"\ufffd".encode, "utf-16be", "add_utf16_bytes")
    raises(UnicodeDecodeError, u"\ufffd".encode, "utf-32be", "add_utf32_bytes")
