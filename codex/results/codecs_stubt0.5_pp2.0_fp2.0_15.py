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
# Test the error handling behaviour of the UTF-8 codec

def test_utf8_errors(s, err, exc, expected):
    try:
        u = s.decode('utf-8', errors=err)
    except exc as e:
        u = e.object
    assert u == expected

def test_utf8_errors_valid(s):
    test_utf8_errors(s, 'strict', UnicodeDecodeError, s)
    test_utf8_errors(s, 'replace', UnicodeDecodeError, s)
    test_utf8_errors(s, 'ignore', UnicodeDecodeError, s)
    test_utf8_errors(s, 'add_one_codepoint', UnicodeDecodeError, s + 'a')
    test_utf8_errors(s, 'add_utf16_bytes', UnicodeDecodeError, s + 'ab')
    test_utf8_errors(s, 'add_utf32_bytes', UnicodeDecodeError, s + 'abcd')

def test_utf8_errors_invalid(
