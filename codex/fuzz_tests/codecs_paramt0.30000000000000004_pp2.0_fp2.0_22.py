import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.test_dir = os.path.dirname(os.path.realpath(__file__))

    def test_run(self):
        test_file_path = os.path.join(self.test_dir, 'test.csv')
        test_file = codecs.open(test_file_path, 'r', 'utf-8', 'strict')
        test_file_content = test_file.read()
        test_file.close()

        expected_file_path = os.path.join(self.test_dir, 'expected.csv')
        expected_file = codecs.open(expected_file_path, 'r', 'utf-8', 'strict')
        expected_file_content = expected_file.read()
        expected_file.close()

        self.assertEqual(expected_file_content, test_file_content)
