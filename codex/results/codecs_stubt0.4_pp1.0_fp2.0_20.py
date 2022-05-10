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

class TestUnicodeDecode(unittest.TestCase):
    def test_decode_error_end(self):
        # Issue #19098: decoding errors should not be raised at the end of the
        # data, but at the first invalid byte.
        self.assertEqual(b'\xff'.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(b'\xff'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xff'.decode('utf-8', 'backslashreplace'), '\\xff')
        self.assertEqual(b'\xff'.decode('utf-8', 'xmlcharrefreplace'), '&#255;')
        self.assertEqual(b'\xff'.decode('utf-8', 'namereplace'), '\\ufffd')

        self.assertEqual(b'\xff'.decode('utf-8', 'strict'),
                         self.assertRaises(UnicodeDecodeError, b'\xff'.decode, '
