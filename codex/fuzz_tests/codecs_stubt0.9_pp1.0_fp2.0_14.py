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


class UnicodeTest(unittest.TestCase):
    def test_decode_various_encodings(self):
        self.assertEqual('Pyth\xf6n', 'Pyth\xc3\xb6n'.decode('utf-8'))
        self.assertEqual('Pyth\xc3\xb6n', 'Pyth\xc3\xb6n'.decode('utf-8-variants'))
        self.assertEqual(u'Pyth\xf6n', u'Pyth\xf6n'.encode('iso-8859-1').decode('iso-8859-1'))
        self.assertEqual(u'Pyth\xf6n', u'Pyth\xf6n'.encode('iso-8859-15').decode('iso-8859-15'))
        self.assertEqual(u'Pyth\u0131n', u'Pyth\u0131n'.encode('iso-8859-9').decode('iso-8859-9'))
        self.assertEqual(
