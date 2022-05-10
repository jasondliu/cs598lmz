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
    # Error handling
    assert codecs.charmap_encode("abc", "strict", {97: None})[0] == b"a"
    assert codecs.charmap_encode("abc", "replace", {97: None})[0] == b"?bc"
    assert codecs.charmap_encode("abc", "ignore", {97: None})[0] == b"bc"
    assert codecs.charmap_encode("abc", "xmlcharrefreplace", {97: None})[0] == b"&#97;bc"
    assert codecs.charmap_encode("abc", "backslashreplace", {97: None})[0] == b"\\x61bc"
    assert codecs.charmap_encode("abc", "add_one_codepoint", {97: None})[0] == b"aabc"
    assert codecs.charmap_encode("abc", "add_utf16_bytes", {97: None})[0] == b"ababc
