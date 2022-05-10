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

class TestDecodingUTF16(unittest.TestCase):
    def test_surrogate_lone(self):
        self.assertRaises(UnicodeDecodeError,
                          '\ud800'.encode, 'utf-16')
        s = '\ud800'
        with self.assertRaises(UnicodeDecodeError) as cm:
            s.encode('utf-16')
        self.assertEqual(cm.exception.object, '\ud800'.encode('utf-16'))
        self.assertEqual(cm.exception.start, 0)

        # These are the current UTR #26 results, but there's some talk
        # of changing them.
        with self.assertRaises(UnicodeDecodeError) as cm:
            s.encode("utf-16-le", "replace")
        self.assertEqual(cm.exception.object, b'\x00\xd8')
        self.assertEqual(cm.exception.start, 0)
        self.assertEqual(s
