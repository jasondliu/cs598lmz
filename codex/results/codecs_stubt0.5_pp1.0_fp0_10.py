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

class CodecsModuleTest(unittest.TestCase):

    def test_encode_decode_error(self):
        for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
            self.assertEqual("abc", codecs.decode("abc", encoding))
            self.assertEqual("abc", codecs.decode("abc", encoding, 'strict'))
            self.assertEqual("abc", codecs.encode("abc", encoding))
            self.assertEqual("abc", codecs.encode("abc", encoding, 'strict'))

            self.assertRaises(UnicodeDecodeError, codecs.decode, b'\xff', encoding)
            self.assertRaises(UnicodeDecodeError, codecs.decode, b'\xff', encoding, 'strict')
            self.assertRaises(UnicodeEncodeError, codecs.encode, "\uffff", encoding)
            self.assertRaises(UnicodeEncodeError, codec
