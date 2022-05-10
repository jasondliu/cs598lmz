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
    for encoding in ("utf-8", "UTF-8"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input, expected in [
                (b"abc", "abc"),
                (b"\xff", "\ufffd"),
                (b"\xff\xff", "\ufffd\ufffd"),
                (b"\xff\xff\xff", "\ufffd\ufffd\ufffd"),
                (b"\xff\xff\xff\xff", "\ufffd\ufffd\ufffd\ufffd"),
                (b"\xff\xff\xff\xff\xff", "\ufffd\ufffd\ufffd\ufffd\ufffd"),
                (b"\xff\xff\xff\xff\xff\xff", "\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd"),
                (b"\xff\xff\xff\xff\xff\xff
