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

class TestDecode(unittest.TestCase):
    def test_decode(self):
        for encoding in ['utf-8', 'utf-16', 'utf-32']:
            for errors in ['strict', 'replace', 'ignore', 'add_one_codepoint',
                           'add_utf16_bytes', 'add_utf32_bytes']:
                s = b'\x80'
                self.assertRaises(UnicodeDecodeError, s.decode, encoding, errors)
                s = b'\x80\x80'
                self.assertRaises(UnicodeDecodeError, s.decode, encoding, errors)
                s = b'\x80\x80\x80'
                self.assertRaises(UnicodeDecodeError, s.decode, encoding, errors)
                s = b'\x80\x80\x80\x80'
                self.assertRaises(UnicodeDecodeError, s.decode, encoding, errors)

class TestEncode(unittest.Test
