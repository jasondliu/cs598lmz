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


def test_unicode_encode_error():
    def check(exc, encoding, expected):
        assert str(exc) == expected
        assert exc.encoding == encoding
        assert exc.object == s
        assert exc.start == 0
        assert exc.end == len(s)
        assert exc.reason == "surrogates not allowed"
        assert exc.args == (s, 0, len(s), "surrogates not allowed")

    s = chr(0xdc00)
    check(UnicodeEncodeError("ascii", s, 0, 1, "surrogates not allowed"),
          "ascii",
          "'ascii' codec can't encode character '\\udc00' in position 0: "
          "surrogates not allowed")
    check(UnicodeEncodeError("ascii", s, 0, 1, "surrogates not allowed", 1),
          "ascii",
          "'ascii' codec can't encode character '\\udc00' in position 0: "
          "surrogates not allowed (1
