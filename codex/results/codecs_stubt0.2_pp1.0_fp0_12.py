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
    # Test UTF-16 codec
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes"):
            for input, expected in (
                (b'\xff\xfea\x00b\x00c\x00', 'abc'),
                (b'\xfe\xff\x00a\x00b\x00c', 'abc'),
                (b'\xff\xfea\x00b\x00\x00\x00', 'ab'),
                (b'\xfe\xff\x00a\x00b\x00\x00', 'ab'),
                (b'\xff\xfea\x00b\x00\x00\x00\x00\x00', 'ab'),
                (b'\xfe\xff\x00a\x00b\x00\x00\x00\x00
