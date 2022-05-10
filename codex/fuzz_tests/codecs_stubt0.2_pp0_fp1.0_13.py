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
    # Test UTF-8
    for encoding in ('utf-8', 'utf_8'):
        for i in range(0xD800, 0xE000):
            # Test decoding
            with self.assertRaises(UnicodeDecodeError) as cm:
                codecs.decode(bytes([i]), encoding)
            self.assertEqual(cm.exception.object, bytes([i]))
            self.assertEqual(cm.exception.start, 0)
            self.assertEqual(cm.exception.end, 1)
            self.assertEqual(cm.exception.reason, 'illegal UTF-8 sequence')
            self.assertEqual(cm.exception.encoding, encoding)
            self.assertEqual(cm.exception.args, (bytes([i]), 0, 1, 'illegal UTF-8 sequence'))
            self.assertEqual(cm.exception.with_traceback(None), cm.exception)
            self.assertEqual(cm.exception.__cause__, None)
