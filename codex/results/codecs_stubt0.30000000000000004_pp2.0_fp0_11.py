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
    # Test UTF-16 and UTF-32 codecs with surrogatepass error handler
    for encoding in ("utf-16", "utf-32"):
        try:
            codecs.lookup_error("surrogatepass")
        except LookupError:
            continue
        for input, output in (
            (b'\x00\x00\x00\x00\x00\x00\x00\x00', "\U00000000"),
            (b'\x00\x00\x00\x00\x00\x00\x00\x01', "\U00000001"),
            (b'\x00\x00\x00\x00\x00\x00\x00\x02', "\U00000002"),
            (b'\x00\x00\x00\x00\x00\x00\x00\x03', "\U00000003"),
            (b'\x00\x00\x00\x00\x00\x00\x00\x04', "\U00000004"),
            (
