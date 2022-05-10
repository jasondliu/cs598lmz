import codecs
codecs.register_error('strict', codecs.raise_error)


class TestRead(unittest.TestCase):

    def test_read_lines(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_file', 'test.txt')
        lines = read.read_lines(file_path)
        self.assertEqual(len(lines), 4)
        self.assertEqual(lines[0], '1')
        self.assertEqual(lines[1], '2')
        self.assertEqual(lines[2], '3')
        self.assertEqual(lines[3], '4')

    def test_read_lines_encoding(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_file', 'test_encoding.txt')
        lines = read.read_lines(file_path, encoding='utf-16')
        self.assertEqual(len(lines), 4)
        self.assertEqual(lines[0], '1')

