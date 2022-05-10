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

def test_utf8_decode(test):
    test.assertEqual(b"\xc3\x28".decode('utf-8', 'strict'),
                     u"\ufffd(")
    test.assertEqual(b"\xa0\xa1".decode('utf-8', 'strict'),
                     u"\ufffd\ufffd")
    test.assertEqual(b"\xe2\x28\xa1".decode('utf-8', 'strict'),
                     u"\ufffd(")
    test.assertEqual(b"\xe2\x82\x28".decode('utf-8', 'strict'),
                     u"\ufffd(")
    test.assertEqual(b"\xf0\x90\x28\xbc".decode('utf-8', 'strict'),
                     u"\ufffd(")
    test.assertEqual(b"\xf0\x28\x8c\xbc".decode('utf-8', 'strict'),
                     u"\ufffd(
