import codecs
# Test codecs.register_error('ignore_stderr', 'ignore')
class StderrTest(unittest.TestCase):
    def test_ignore_errors(self):
        text = 'abc\xe0def\xe7'
        self.assertRaises(UnicodeError, text.encode, 'utf-7', 'ignore')
        self.assertEqual(text.encode('utf-7', 'ignore_stderr'), text.encode(
            'utf-7', 'ignore'))
        self.assertRaises(TypeError, codecs.register_error, 'foo')


class CodecsModuleTest(unittest.TestCase):
    """Test the codecs module itself."""

    def test_search_function(self):
        """Test the search_function for the builtin codecs."""
        for enc in ('utf-8', 'unicode-escape', 'iso-8859-1'):
            self.assertIsNotNone(codecs.getencoder(enc), 'No encoder for %s' %
                enc)
        for dec in ('utf-8
