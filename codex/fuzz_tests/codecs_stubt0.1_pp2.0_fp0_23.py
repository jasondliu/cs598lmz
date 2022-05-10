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
                (b"\xc0\x81", "\ufffd"),
                (b"\xc1\x80", "\ufffd"),
                (b"\xc1\x81", "\ufffd"),
                (b"\xc2\x80", "\u0080"),
                (b"\xc2\x81", "\u0081"),
                (b"\xc2\xbf", "\u00bf"),
                (b"\xc3\x80", "\u00c0"),
                (b"\xc3\x81", "\u00c1"),
                (b"\xc3\xbf", "\u00df"),
                (b"\xc4\x80
