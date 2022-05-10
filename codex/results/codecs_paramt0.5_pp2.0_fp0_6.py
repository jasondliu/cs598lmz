import codecs
codecs.register_error('strict', codecs.ignore_errors)


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_empty(self):
        self.assertEqual(self.parser.parse(''), [])

    def test_comment(self):
        self.assertEqual(self.parser.parse('#test'), [])

    def test_simple(self):
        self.assertEqual(self.parser.parse('test'), ['test'])

    def test_two_words(self):
        self.assertEqual(self.parser.parse('test test'), ['test', 'test'])

    def test_two_words_with_space(self):
        self.assertEqual(self.parser.parse('test   test'), ['test', 'test'])

    def test_two_words_with_tab(self):
        self.assertEqual(self.parser.parse('test\ttest'), ['test', 'test'])

    def test_two_words_with_newline(
