import codecs
# Test codecs.register_error('test', codecs.replace_errors)
# Test codecs.lookup_error('test')

class TestCodecs(unittest.TestCase):
    # There are more codecs tests in test_textwrap and test_normalization.

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_encode('\xe4\xf6\xfc')[0],
                         b'\xc3\xa4\xc3\xb6\xc3\xbc')
        self.assertEqual(codecs.utf_8_encode('\u20ac')[0], b'\xe2\x82\xac')
        self.assertEqual(codecs.utf_8_encode('\U0001d120')[0],
                         b'\xf0\x9d\x84\xa0')
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa4\xc3\xb6\xc3\xbc')[0],
                         '\
