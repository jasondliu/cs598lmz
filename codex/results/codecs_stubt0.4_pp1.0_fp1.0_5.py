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
    # UTF-8
    for i in range(0xD800, 0xE000):
        assert codecs.utf_8_decode(bytes([0xED, i >> 8, i & 0xFF]), "replace") == ("\ufffd", 3)
        assert codecs.utf_8_decode(bytes([0xED, i >> 8, i & 0xFF]), "ignore") == ("", 3)
        assert codecs.utf_8_decode(bytes([0xED, i >> 8, i & 0xFF]), "xmlcharrefreplace") == ("&#%d;" % i, 3)
        assert codecs.utf_8_decode(bytes([0xED, i >> 8, i & 0xFF]), "backslashreplace") == ("\\U%08X" % i, 3)
        assert codecs.utf_8_decode(bytes([0xED, i >> 8, i & 0xFF]), "add_one_codepoint") == ("a", 3)
        assert codecs.utf_8
