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
    # test UTF-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes"):
            for s in ("abc", "\u20ac", "\u20ac\u20ac", "\u20ac\u20ac\u20ac"):
                for i in range(len(s)):
                    b = s.encode(enc, errors)
                    assert b.decode(enc, errors) == s
                    assert b[:i].decode(enc, errors) == s[:i]
                    assert b[i:].decode(enc, errors) == s[i:]
                    assert b[:i+1].decode(enc, errors) == s[:i+1]
                    assert b[i+1:].decode(enc, errors) == s[i+1:]

    # test UTF-32
    for enc in ("utf-32
