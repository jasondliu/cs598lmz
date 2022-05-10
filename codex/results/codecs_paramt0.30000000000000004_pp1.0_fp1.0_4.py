import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_data_dir = os.path.join(self.test_dir, 'test_data')
        self.test_output_dir = os.path.join(self.test_dir, 'test_output')
        self.test_temp_dir = os.path.join(self.test_dir, 'test_temp')
        self.test_input_dir = os.path.join(self.test_dir, 'test_input')
        self.test_input_file = os.path.join(self.test_input_dir, 'test_input.txt')
        self.test_output_file = os.path.join(self.test_output_dir, 'test_output.txt')
        self.test_temp_file = os.path.join(self.test_temp_dir, 'test_temp
