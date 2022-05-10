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
    # Test UTF-16
    for enc in ("utf-16", "utf-16-be", "utf-16-le"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"):
            for i in range(0, 0x110000, 0x100):
                c = chr(i)
                b = c.encode(enc, errors)
                c2 = b.decode(enc, errors)
                if errors == "strict":
                    if i > 0x10ffff:
                        assert c2 == "\ufffd"
                    else:
                        assert c2 == c
                else:
                    assert c2 == c

    # Test UTF-32
    for enc in ("utf-32", "utf-32-be", "utf-32-le"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf32_bytes"):
            for i in range(0, 0x110000
