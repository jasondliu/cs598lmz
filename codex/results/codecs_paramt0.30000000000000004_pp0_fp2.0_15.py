import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8_to_utf16(self):
        self.assertEqual(utf8_to_utf16(b'\x00\x00\x00\x00'), b'\x00\x00\x00\x00')
        self.assertEqual(utf8_to_utf16(b'\x00\x00\x00\x00\x00\x00\x00\x00'), b'\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(utf8_to_utf16(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(
