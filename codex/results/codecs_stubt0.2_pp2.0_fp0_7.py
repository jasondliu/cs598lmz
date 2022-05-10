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
    for i in range(0xD800, 0xE000):
        try:
            b"\xed\xa0\x80".decode("utf-8", "strict")
        except UnicodeDecodeError as exc:
            assert exc.object == b"\xed\xa0\x80"
            assert exc.start == 0
            assert exc.end == 3
            assert exc.reason == "surrogates not allowed"
            assert exc.encoding == "utf-8"
            assert exc.args == (b"\xed\xa0\x80", 0, 3, "surrogates not allowed")
            assert str(exc) == "'utf-8' codec can't decode byte 0xed in position 0: surrogates not allowed"
            assert exc.__class__ == UnicodeDecodeError

        try:
            b"\xed\xa0\x80".decode("utf-8", "replace")
        except UnicodeDecodeError as exc:
            assert exc.object == b"\x
