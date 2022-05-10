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

#
#   Test cases
#
def test_utf16_be_decode(encoding):
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', "replace") == ('abc', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', "ignore") == ('ac', 4)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', "add_one_codepoint") == ('aabc', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', "add_utf16_bytes") == ('aabcc', 8)
    raises(UnicodeDecodeError, codecs.utf_
