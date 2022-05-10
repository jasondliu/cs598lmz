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

class TestCodecRegressions(unittest.TestCase):

    def test_issue2907(self):
        # UTF-8 codec should reject surrogates
        self.assertRaises(UnicodeEncodeError, '\ud800'.encode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, b'\xed\xa0\x80'.decode, 'utf-8')

    def test_issue1628(self):
        # UTF-7 codec should reject surrogates
        self.assertRaises(UnicodeEncodeError, '\ud800'.encode, 'utf-7')
        self.assertRaises(UnicodeDecodeError, b'+AAA-'.decode, 'utf-7')

    def test_issue2982(self):
        # make sure UTF-7 accepts the string "C++"
        self.assertEqual('C++'.encode('utf-7'), b'C++')

    def test_issue4710(self):
        # UTF-7 should reject more than 8 bits per character
