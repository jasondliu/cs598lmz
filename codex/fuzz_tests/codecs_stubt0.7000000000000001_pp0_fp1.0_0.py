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

class Test_Decode(unittest.TestCase):
    def test_latin1(self):
        self.assertEqual(codecs.decode(b'abc', 'latin1'), 'abc')
        self.assertEqual(codecs.decode(b'\xc3\xa4', 'latin1'), '\xe4')

    def test_utf8(self):
        self.assertEqual(codecs.decode(b'abc', 'utf8'), 'abc')
        self.assertEqual(codecs.decode(b'\xc3\xa4', 'utf8'), '\xe4')
        self.assertEqual(codecs.decode(b'\xc3\x9f', 'utf8'), '\xdf')
        self.assertEqual(codecs.decode(b'\xff', 'utf8', 'strict'),
                         UnicodeDecodeError('utf8', b'\xff', 0, 1, 'invalid continuation byte'))
        self.assertEqual(codecs
