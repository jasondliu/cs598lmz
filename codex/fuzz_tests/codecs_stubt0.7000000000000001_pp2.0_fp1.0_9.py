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

def test_errorhandler_codepoint():
    s = codecs.encode("abc\xff", 'utf-8', 'add_one_codepoint')
    assert s == b"abca\xc3\xbf"

def test_errorhandler_bytes():
    s = codecs.encode("abc\xff", 'utf-16', 'add_utf16_bytes')
    assert s == b"\xff\xfea\x00b\x00c\x00\x00\xff\x00"
    s = codecs.encode("abc\xff", 'utf-32', 'add_utf32_bytes')
    assert s == b"\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00\x00\x00\xff\x00"
