import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_File(unittest.TestCase):
    def test_open_file(self):
        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(__file__), 'test.txt')))

    def test_read_file(self):
        with open(os.path.join(os.path.dirname(__file__), 'test.txt'), 'r') as f:
            self.assertEqual(f.read(), 'Hello World!\n')

    def test_write_file(self):
        with open(os.path.join(os.path.dirname(__file__), 'test.txt'), 'w') as f:
            f.write('Hello World!\n')

    def test_read_file_with_codecs(self):
        with codecs.open(os.path.join(os.path.dirname(__file__), 'test.txt'), 'r', 'utf-8', 'strict') as f:
           
