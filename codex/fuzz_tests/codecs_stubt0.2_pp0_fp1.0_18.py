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
    for encoding in ("utf-8", "utf_8"):
        # Check that the codecs module can be used to encode and decode
        # UTF-8.
        s = "abc\u1234\u20ac\u8000"
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            try:
                x = s.encode(encoding, errors)
                y = x.decode(encoding, errors)
            except UnicodeEncodeError:
                if errors in ("strict", "replace", "ignore"):
                    raise
                else:
                    continue
            if errors == "strict":
                assert x == b'abc\xe1\x88\xb4\xe2\x82\xac\xe8\x80\x80'
                assert y == s
            elif errors == "replace":
                assert x == b'abc\xe1\x
