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

# Test UTF-8

import encodings.utf_8

def test_utf8_decode(s, expected):
    assert encodings.utf_8.decode(s, "strict") == expected
    assert encodings.utf_8.decode(s, "replace") == expected.replace("\ufffd", "?")
    assert encodings.utf_8.decode(s, "ignore") == expected.replace("\ufffd", "")
    assert encodings.utf_8.decode(s, "add_one_codepoint") == expected.replace("\ufffd", "a")
    assert encodings.utf_8.decode(s, "add_utf16_bytes") == expected.replace("\ufffd", "ab")
    assert encodings.utf_8.decode(s, "add_utf32_bytes") == expected.replace("\ufffd", "abcd")

def test_utf8_encode(s, expected):
    assert encodings.utf_8.encode(s
