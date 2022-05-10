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
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "surrogateescape", "surrogatepass"):
            for input, expected in [
                (b'\xff', u'\ufffd'),
                (b'\xff\xfe', u'\ufffd\ufffd'),
                (b'\xff\xfe\x00', u'\ufffd\ufffd\x00'),
                (b'\xff\xfe\x00\x00', u'\ufffd\ufffd\x00\x00'),
                (b'\xff\xfe\x00\x00\x00', u'\ufffd\ufffd\x00\x00\x00'),
                (b'\xff\xfe\x00\x00\x00\x00', u'\ufffd\ufffd\x00\x00\x00\x00'),
                (b
