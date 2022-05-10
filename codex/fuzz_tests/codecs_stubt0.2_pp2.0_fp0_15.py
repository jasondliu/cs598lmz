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

def test_utf8(s, enc, dec):
    assert s.encode(enc) == s.encode(enc, "strict")
    assert s.encode(enc) == s.encode(enc, "replace")
    assert s.encode(enc) == s.encode(enc, "ignore")
    assert s.encode(enc) == s.encode(enc, "xmlcharrefreplace")
    assert s.encode(enc) == s.encode(enc, "backslashreplace")
    assert s.encode(enc) == s.encode(enc, "namereplace")
    assert s.encode(enc) == s.encode(enc, "surrogateescape")
    assert s.encode(enc) == s.encode(enc, "surrogatepass")
    assert s.encode(enc) == s.encode(enc, "add_one_codepoint")
    assert s.encode(enc) == s.encode(enc, "add_utf16_bytes")
    assert s.en
