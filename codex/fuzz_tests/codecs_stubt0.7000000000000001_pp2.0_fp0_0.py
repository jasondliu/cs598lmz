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

def check_unicode_decode(input, errors, expected):
    result = input.decode("utf-16", errors)
    assert result == expected

def check_unicode_encode(input, errors, expected):
    result = input.encode("utf-16", errors)
    assert result == expected

def test_unicode_decode():
    check_unicode_decode(b'\xff\xff', "ignore", "")
    check_unicode_decode(b'\xff\xff', "replace", u"\ufffd")
    check_unicode_decode(b'\xff\xff', "add_one_codepoint", u"a")
    check_unicode_decode(b'\xff\xff', "add_utf16_bytes", u"aba")
    check_unicode_decode(b'\xff\xff', "add_utf32_bytes", u"abcd")

def test_unicode_encode():
    check_unicode_encode(u"\ufffd\ufffd", "
