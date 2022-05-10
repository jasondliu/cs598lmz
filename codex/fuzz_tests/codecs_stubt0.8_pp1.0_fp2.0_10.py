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

@cpython_only
class TestUTF8(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual(u'abc'.encode('utf-8'), b'abc')

    def test_2(self):
        self.assertEqual(u'\u00fc'.encode('utf-8'), b'\xC3\xBC')

    def test_3(self):
        self.assertEqual(u'\U0001d11e'.encode('utf-8'), b'\xF0\x9D\x84\x9E')

    def test_4(self):
        self.assertEqual(u'\U0010FFFD'.encode('utf-8'), b'\xF4\x8F\xBF\xBD')

    def test_error_strict(self):
        self.assertRaises(UnicodeEncodeError, u'\U00110000'.encode, 'utf-8')

    def test_error_replace(self):
        self.assertE
