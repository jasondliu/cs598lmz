import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):

    def test_simple_ascii(self):
        """Test simple ASCII."""
        self.assertEqual(
            'abc',
            utils.to_unicode('abc'))

    def test_simple_utf8(self):
        """Test simple UTF-8."""
        self.assertEqual(
            u'\u00e9',
            utils.to_unicode('\xc3\xa9'))

    def test_simple_latin1(self):
        """Test simple Latin-1."""
        self.assertEqual(
            u'\u00e9',
            utils.to_unicode('\xe9', 'latin-1'))

    def test_simple_utf16(self):
        """Test simple UTF-16."""
        self.assertEqual(
            u'\u00e9',
            utils.to_unicode('\xff\xfe\xe9\x00', 'utf-16
