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

def test_unicode_escape_decode_errors(test):
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "strict")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "replace")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "ignore")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "add_one_codepoint")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "add_utf16_bytes")
    test.assertRaises(UnicodeDecodeError, "\xe9".decode, "unicode-escape", "add_utf32_bytes")

def test_unicode
