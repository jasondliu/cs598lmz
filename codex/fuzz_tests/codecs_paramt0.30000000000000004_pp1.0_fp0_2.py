import codecs
codecs.register_error('strict', codecs.ignore_errors)

class TestUtil(unittest.TestCase):
    def test_get_encoding(self):
        self.assertEqual(util.get_encoding('/path/to/file.txt'), 'utf-8')
        self.assertEqual(util.get_encoding('/path/to/file.txt', 'utf-8'), 'utf-8')
        self.assertEqual(util.get_encoding('/path/to/file.txt', 'utf-16'), 'utf-16')
        self.assertEqual(util.get_encoding('/path/to/file.txt', 'utf-16'), 'utf-16')
        self.assertEqual(util.get_encoding('/path/to/file.txt', 'utf-16'), 'utf-16')
        self.assertEqual(util.get_encoding('/path/to/file.txt', 'utf-16'), 'utf-16')
        self.assertEqual(util.get_encoding('/path/to/
