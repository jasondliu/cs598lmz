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
    with support.check_warnings(("", UnicodeWarning)):
        # test UTF-16
        for encoding in ("utf-16", "utf-16-be", "utf-16-le"):
            # test decoding
            for input, output in (
                (b'\xff\xfe\x61\x00', "a"),
                (b'\x61\x00', "a"),
                (b'\x61\x00\x62\x00', "ab"),
                (b'\x61\x00\x00\x00', "a"),
                (b'\x61\x00\x00\x00\x62\x00', "ab"),
                (b'\x61\x00\x00\x00\x00\x00', "a"),
                (b'\x61\x00\x00\x00\x00\x00\x62\x00', "ab"),
                (b'\x61\x00\x00\x00\x00\x00
