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
    # Test the UTF-8 codec
    for encoding in ("utf-8", "UTF-8"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input, expected in (
                (b"abc\xff", "abc\ufffd"),
                (b"abc\xff\xff", "abc\ufffd\ufffd"),
                (b"abc\xff\xff\xff", "abc\ufffd\ufffd\ufffd"),
                (b"abc\xff\xff\xff\xff", "abc\ufffd\ufffd\ufffd\ufffd"),
                (b"abc\xff\xff\xff\xff\xff", "abc\ufffd\ufffd\ufffd\ufffd\ufffd"),
                (b"abc\xc0", "abc\ufffd"),
                (b"abc\xc0\xc0", "abc\ufffd\ufffd"),
                (b"abc\xc0
