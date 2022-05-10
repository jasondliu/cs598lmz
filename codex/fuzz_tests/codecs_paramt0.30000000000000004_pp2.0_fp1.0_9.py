import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_utils(unittest.TestCase):
    def test_get_file_path(self):
        path = utils.get_file_path('test.txt')
        self.assertEqual(path, './test.txt')

    def test_get_file_path_with_path(self):
        path = utils.get_file_path('test.txt', './')
        self.assertEqual(path, './test.txt')

    def test_get_file_path_with_path_and_file(self):
        path = utils.get_file_path('test.txt', './test')
        self.assertEqual(path, './test/test.txt')

    def test_get_file_path_with_path_and_file_and_extension(self):
        path = utils.get_file_path('test.txt', './test', 'txt')
        self.assertEqual(path, './test/test.txt')

    def test
