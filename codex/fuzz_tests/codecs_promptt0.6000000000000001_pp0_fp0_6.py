import codecs
# Test codecs.register_error() and codecs.lookup_error()
import encodings.ascii
# Test codecs.register() and codecs.lookup()
import encodings.idna
# Test codecs.register() and codecs.lookup()
import encodings.utf_8
# Test codecs.register() and codecs.lookup()


class UTF8TestCase(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(b'\xc3\xbc'.decode('utf-8'), '\xfc')
        self.assertEqual('\xfc'.encode('utf-8'), b'\xc3\xbc')

    def test_utf8_error(self):
        self.assertRaises(UnicodeError, b'\xc3\x28'.decode, 'utf-8')

    def test_utf8_decode(self):
        self.assertEqual('La Pe\xf1a', 'La Pe\xc3\xb1a'.decode('utf-8'))
        self
