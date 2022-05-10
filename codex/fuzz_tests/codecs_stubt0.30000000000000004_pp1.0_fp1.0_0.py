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

def test_utf16_decode():
    # test decoding of UTF-16 with BOM
    for bom in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
        assert codecs.utf_16_decode(bom + b"abc", "ignore") == ("abc", 2)
        assert codecs.utf_16_decode(bom + b"abc", "replace") == ("abc", 2)
        assert codecs.utf_16_decode(bom + b"abc", "backslashreplace") == ("abc", 2)
        assert codecs.utf_16_decode(bom + b"abc", "xmlcharrefreplace") == ("abc", 2)
        assert codecs.utf_16_decode(bom + b"abc", "strict") == ("abc", 2)
        assert codecs.utf_16_decode(bom + b"ab\xffc", "ignore") == ("abc", 4)
        assert codecs.utf_16_decode(bom + b"ab
