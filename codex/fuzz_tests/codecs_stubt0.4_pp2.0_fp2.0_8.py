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
    # encoding
    assert codecs.charmap_encode("abc") == (b'abc', 3)
    assert codecs.charmap_encode("abc", "strict") == (b'abc', 3)
    assert codecs.charmap_encode("abc", "ignore") == (b'abc', 3)
    assert codecs.charmap_encode("abc", "replace", {97: None}) == (b'\x00bc', 3)
    # error handling
    raises(UnicodeEncodeError, codecs.charmap_encode, "abc\u1234", "strict", {97: None})
    assert codecs.charmap_encode("abc\u1234", "ignore", {97: None}) == (b'\x00bc\u1234', 5)
    assert codecs.charmap_encode("abc\u1234", "replace", {97: None}) == (b'\x00bc?', 5)
    assert codecs.charmap_en
