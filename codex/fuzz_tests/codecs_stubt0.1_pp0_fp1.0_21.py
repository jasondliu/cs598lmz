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
    # Test UTF-8
    for encoding in ("utf-8", "utf_8"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint"):
            for input, expected in (
                (b"\x80", "\ufffd"),
                (b"\xc0\x80", "\ufffd"),
                (b"\xc0\xaf", "\ufffd"),
                (b"\xc0\xbf", "\ufffd"),
                (b"\xc1\x80", "\ufffd"),
                (b"\xc1\xbf", "\ufffd"),
                (b"\xc2\x80", "\ufffd"),
                (b"\xc2\xbf", "\ufffd"),
                (b"\xc3\x80", "\ufffd"),
                (b"\xc3\xbf", "\ufffd"),
                (b"\xc4\x80", "\ufffd"),
                (b"\xc4\xbf", "\ufffd"),
                (
