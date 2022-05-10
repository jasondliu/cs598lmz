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

class TestUtf16(unittest.TestCase):
    def test_utf16_decode(self):
        self.assertEqual(unicode(b'\xff\xfea\x00b\x00', "utf-16"), u"ab")

    def test_utf16_encode(self):
        self.assertEqual(u"ab".encode("utf-16"), b'\xff\xfea\x00b\x00')

    def test_utf16_le_decode(self):
        self.assertEqual(unicode(b'\xfe\xff\x00a\x00b', "utf-16-le"), u"ab")

    def test_utf16_le_encode(self):
        self.assertEqual(u"ab".encode("utf-16-le"), b'\xfe\xff\x00a\x00b')

    def test_utf16_be_decode(self):
        self.assertEqual(unicode(b'\xff\xfe\x00a\
