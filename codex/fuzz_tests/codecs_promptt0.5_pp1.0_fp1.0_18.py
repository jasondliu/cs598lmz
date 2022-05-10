import codecs
# Test codecs.register_error
import warnings

# The ones we need for the tests
from encodings import utf_8, utf_16, utf_16_le, utf_16_be, utf_32, \
     utf_32_le, utf_32_be, ascii

class TestUTF(unittest.TestCase):
    def test_utf8(self):
        u = '\u20ac'
        for i in range(1, len(u)):
            self.assertRaises(UnicodeDecodeError,
                              u.encode, 'utf-8', 'strict')

        self.assertEqual(u.encode('utf-8'), b'\xe2\x82\xac')
        self.assertEqual(u.encode('utf-8', 'strict'), b'\xe2\x82\xac')
        self.assertEqual(u.encode('utf-8', 'replace'), b'?\xe2\x82\xac')
        self.assertEqual(u.encode('utf
