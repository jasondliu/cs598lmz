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
    test_unicode_internal_encode()
    test_unicode_internal_decode()

def test_unicode_internal_encode():
    # test unicode_internal_encode()
    for encoding in ("utf-16-be", "utf-16-le", "utf-32-be", "utf-32-le"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            # test encoding
            u = chr(0xdc00)
            s = u.encode(encoding, errors)
            if errors == "strict":
                raises(UnicodeError, u.encode, encoding, errors)
            elif errors == "replace":
                assert s == b'?\x00'
            elif errors == "ignore":
                assert s == b'\x00'
            elif errors == "add_one_codepoint":
                assert s == b'a\
