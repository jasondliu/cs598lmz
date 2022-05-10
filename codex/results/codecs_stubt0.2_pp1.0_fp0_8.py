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
    # Test that the UTF-16 and UTF-32 codecs can handle surrogates
    # properly.
    for encoding in ("utf-16", "utf-16-le", "utf-16-be",
                     "utf-32", "utf-32-le", "utf-32-be"):
        # Encode a surrogate pair
        s = "\ud800\udc00"
        b = s.encode(encoding)
        # Decode the surrogate pair
        s2 = b.decode(encoding)
        assert s == s2
        # Decode a single surrogate
        for i in range(len(b)):
            b2 = b[:i] + b[i+1:]
            try:
                s2 = b2.decode(encoding)
            except UnicodeDecodeError as exc:
                s2 = b2.decode(encoding, "add_one_codepoint")
            assert len(s2) == 1
            assert ord(s2) >= 0xD800 and ord(s2) <=
