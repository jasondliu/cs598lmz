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

def test_utf_16_be():
    test_cases = (
        (b"\xfe\xff\x00\x00", ""),
        (b"\xfe\xff\x00a", "a"),
        (b"\xfe\xff\x00ab", "ab"),
        (b"\xfe\xff\x00a\x00", "a\x00"),
        (b"\xfe\xff\x00a\x00b", "a\x00b"),
        (b"\xfe\xff\x00a\x00b\x00", "a\x00b\x00"),
        (b"\xfe\xffab", "ab"),
        (b"\xfe\xff\x00\x00\x00\x00", ""),
        (b"\xfe\xff\x00\x00\x00a", "a"),
        (b"\xfe\xff\x00\x00\x00\x00\x00\x00", ""),
        (b"
