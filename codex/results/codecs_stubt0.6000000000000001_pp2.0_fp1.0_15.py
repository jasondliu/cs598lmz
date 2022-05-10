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

# Decoding tests

def test_decode_error_handling():
    # test utf-8
    assert u"\u1234".encode("utf-8", "replace") == "\xe1\x88\xb4"
    assert u"\u1234".encode("utf-8", "xmlcharrefreplace") == "&#4660;"
    assert u"\u1234".encode("utf-8", "backslashreplace") == "\\u1234"
    assert u"\u1234".encode("utf-8", "namereplace") == "\\N{DEVANAGARI LETTER DDA}"

    assert u"\u1234".encode("utf-8", "ignore") == ""
    assert u"\u1234".encode("utf-8", "strict") == "\xe1\x88\xb4"

    # test utf-16
    assert u"\u1234".encode("utf-16", "replace") == "\xff\xfd4"
    assert u"\u1234".encode
