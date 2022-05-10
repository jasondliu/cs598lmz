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

def test_main():
    # Issue #17069: UTF-16 and UTF-32 codecs should not accept surrogates
    # when decoding.
    for codec in ('utf-16', 'utf-16-le', 'utf-16-be',
                  'utf-32', 'utf-32-le', 'utf-32-be'):
        with self.assertRaises(UnicodeDecodeError) as cm:
            u'\ud800'.encode(codec)
        self.assertEqual(cm.exception.start, 0)
        self.assertEqual(cm.exception.end, 1)

        with self.assertRaises(UnicodeDecodeError) as cm:
            u'\udc00'.encode(codec)
        self.assertEqual(cm.exception.start, 0)
        self.assertEqual(cm.exception.end, 1)

        with self.assertRaises(UnicodeDecodeError) as cm:
            u'\ud800\udc00'.encode(codec)

