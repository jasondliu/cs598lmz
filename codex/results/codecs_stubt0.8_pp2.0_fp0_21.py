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

def test_decode_utf8():
    assert b"\xff".decode("utf-8", "strict") == "\ufffd"
    assert b"\xff".decode("utf-8", "ignore") == ""
    assert b"\xff".decode("utf-8", "replace") == "\ufffd"
    assert b"\xff".decode("utf-8", "add_one_codepoint") == "a"
    assert b"\xff".decode("utf-8", "backslashreplace") == "\\ufffd"
    assert b"\xff".decode("utf-8", "xmlcharrefreplace") == "&#255;"
    assert b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "strict") == "\udc00\ud800"
    assert b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "surrogatepass") == "\U00010000"
    raises(UnicodeDec
