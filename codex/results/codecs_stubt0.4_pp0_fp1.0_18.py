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

class Test_UTF8(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual(b'\xf0\x90\x80\x80'.decode('utf-8'),
                         '\U00010000')
        self.assertEqual(b'\xf0\x90\x80\x80'.decode('utf-8',
                                                    'add_one_codepoint'),
                         '\U00010000a')
        self.assertEqual(b'\xf0\x90\x80\x80'.decode('utf-8',
                                                    'add_utf16_bytes'),
                         '\U00010000ab')
        self.assertEqual(b'\xf0\x90\x80\x80'.decode('utf-8',
                                                    'add_utf32_bytes'),
                         '\U00010000abcd')
        self.assertEqual(b'\xf0\x90\x80\x80\xf0\x90\x80\x80
