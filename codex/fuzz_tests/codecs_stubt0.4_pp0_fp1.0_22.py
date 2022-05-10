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

def test_decode(encoding, errors, test_string, expected):
    decoded = test_string.decode(encoding, errors)
    assert decoded == expected

def test_encode(encoding, errors, test_string, expected):
    encoded = test_string.encode(encoding, errors)
    assert encoded == expected

def test_unicode_decode():
    test_decode("ascii", "add_one_codepoint", b"\xff", "a\ufffd")
    test_decode("utf-16", "add_one_codepoint", b"\xff", "a\ufffd")
    test_decode("utf-16-be", "add_one_codepoint", b"\xff", "a\ufffd")
    test_decode("utf-16-le", "add_one_codepoint", b"\xff", "a\ufffd")
    test_decode("utf-32", "add_one_codepoint", b"\xff", "a\ufffd")

