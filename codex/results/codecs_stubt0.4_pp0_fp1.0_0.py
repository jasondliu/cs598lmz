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
    # UTF-8
    for encoding in ("utf-8", "utf_8"):
        # UTF-8: surrogateescape error handler
        for input, expected in [
            (b"\xed\xa0\x80", "\udc80"),
            (b"\xed\xa0\x80\xed\xb0\x80", "\udc80\udc80"),
            (b"\xed\xa0\x80\xed\xb0\x80\xed\xa0\x80", "\udc80\udc80\udc80"),
        ]:
            assert codecs.decode(input, encoding, "surrogateescape") == expected
            assert codecs.decode(input, encoding, "surrogateescape") == expected
            assert codecs.decode(input, encoding, "surrogateescape") == expected
            assert codecs.decode(input, encoding, "surrogateescape") == expected
            assert codecs.decode(input, encoding, "surrogateescape") ==
