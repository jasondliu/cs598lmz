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
    # test utf-16-le
    assert codecs.utf_16_le_decode(b"\x00\x61\x00\x62\x00\x63", "strict") == ("abc", 4)
    assert codecs.utf_16_le_decode(b"\x00\x61\x00\x62\x00\x63", "replace") == ("abc", 4)
    assert codecs.utf_16_le_decode(b"\x00\x61\x00\x62\x00\x63", "ignore") == ("abc", 4)
    assert codecs.utf_16_le_decode(b"\x00\x61\x00\x62\x00\x63", "add_one_codepoint") == ("aabc", 4)
    assert codecs.utf_16_le_decode(b"\x00\x61\x00\x62\x00\x63", "add_utf16_bytes") == ("aabc", 4
