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


class UnicodeDecodeErrorTest(unittest.TestCase):

    def test_decode(self):
        # Simple test: utf-8 encoded
        u = 'pi: \u03c0'
        s = b'pi: \xcf\x80' # (latin-1 encoding is wrong, but it can decode)
        self.assertEqual(u, u.encode('utf-8').decode('utf-8'))
        self.assertRaises(TypeError, codecs.decode, u, 'utf-8')

        # Issue #2580: utf-7 encoded
        self.assertRaises(UnicodeDecodeError, codecs.decode, b'+AOA-gDfAN8-', 'utf-7')

        # Try some errors
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8', 'strict')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8', 'ignore')
        self.assertRaises(Un
