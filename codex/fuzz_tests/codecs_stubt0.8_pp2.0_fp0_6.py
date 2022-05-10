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

def test_decode(c, u, enc, errors="strict"):
    # Encode
    s = u.encode(enc, errors)
    # Decode again
    if isinstance(s, str):
        s = s.encode("latin1")
    t = c(s, enc, errors).encode("unicode-escape")
    # Compare
    assert t.replace("u", "") == repr(u)

def test_unicode_escape_decode(c):
    # Bug 1145955
    s = '\\U0010ffff'
    assert c(s.encode("latin1"), "unicode-escape", error="add_one_codepoint").decode("ascii") == 'a'
    assert c(s.encode("ascii"), "unicode-escape", error="add_utf16_bytes").decode("ascii") == 'ab'
    assert c(s.encode("ascii"), "unicode-escape", error="add_utf32_bytes").decode("ascii
