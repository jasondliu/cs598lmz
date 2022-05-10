import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_utf8(unittest.TestCase):
    def test_utf8(self):
        # http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
        # 2.1 First possible sequence of a certain length
        self.assertEqual(utf8_decode('\x00'), (0x0, 1))
        self.assertEqual(utf8_decode('\xc2\x80'), (0x80, 2))
        self.assertEqual(utf8_decode('\xe0\xa0\x80'), (0x800, 3))
        self.assertEqual(utf8_decode('\xf0\x90\x80\x80'), (0x10000, 4))
        self.assertEqual(utf8_decode('\xf8\x88\x80\x80\x80'), (0x200000, 5))
        self.assertEqual(utf8_decode('\xfc\x
