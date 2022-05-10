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

class TestUTF8(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(b'\xc3\xa9', 'é'.encode('utf-8'))
        self.assertEqual(b'\xe2\x82\xac', '€'.encode('utf-8'))
        self.assertEqual(b'\xf0\x90\x80\x80', '𐀀'.encode('utf-8'))
        self.assertEqual(b'\xf4\x8f\xbf\xbf', '\U0010ffff'.encode('utf-8'))
        self.assertRaises(UnicodeEncodeError, '\U00110000'.encode, 'utf-8')

    def test_decode(self):
        self.assertEqual('é', b'\xc3\xa9'.decode('utf-8'))
        self.assertEqual('€', b'\xe2\x82\xac'.decode('utf-8'))
