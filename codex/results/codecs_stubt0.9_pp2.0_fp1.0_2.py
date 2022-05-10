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

class EncodeTest(unittest.TestCase):
    def test_bug_851123(self):
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc',
                          'äöü'.encode('utf-8', 'ignore'))

    def test_bad_decoding(self):
        for codec in ["base64", "hex", "quopri"]:
            self.assertRaises(UnicodeEncodeError,
                              '\xff'.encode, codec)

    def test_bad_endianness(self):
        self.assertRaises(UnicodeError, '\u1234'.encode, "mbcs")
        self.assertRaises(UnicodeError, '\u1234'.encode, "utf-16-be")
        self.assertRaises(UnicodeError, '\u1234'.encode, "utf-32-le")
        for codec in ["utf-16", "utf-32"]:
            self.assertRaises(Unic
