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

def test_utf8_errors(test):
    # utf-8 errors
    test.assertEqual(b"\xf1\x80\x80\x80".decode("utf-8", "strict"),
                     "\U00100000")
    test.assertRaises(UnicodeDecodeError,
                      b"\xf1\x80\x80".decode, "utf-8", "strict")
    test.assertEqual(b"\xf1\x80\x80".decode("utf-8", "replace"),
                     "\ufffd\ufffd")
    test.assertEqual(b"\xf1\x80\x80".decode("utf-8", "ignore"), "")
    test.assertEqual(b"\xf1\x80\x80".decode("utf-8", "add_one_codepoint"),
                     "\ufffd\U00100000")
    test.assertEqual(b"\xf1\x80\x80".decode("utf-8", "add_utf16_bytes
