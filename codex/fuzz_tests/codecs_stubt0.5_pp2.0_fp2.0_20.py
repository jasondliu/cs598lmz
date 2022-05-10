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

def test_utf8_decode(encoding):
    # test utf-8 decoding
    # first, test all possible error handlers
    for handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
        for input, expected in [
                (b"\x80", "�"),
                (b"\xc0", "�"),
                (b"\xc0\x80", "�"),
                (b"\xc0\xaf", "�"),
                (b"\xc1", "�"),
                (b"\xc1\x80", "�"),
                (b"\xc1\xaf", "�"),
                (b"\xc2", "�"),
                (b"\xc2\x80", "�"),
                (b"\xc2\xaf", "�"),
                (b"\xc3", "�"),
                (b"\xc3\x80", "�"),
                (b"\xc3
