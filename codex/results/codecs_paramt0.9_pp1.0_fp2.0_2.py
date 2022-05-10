import codecs
codecs.register_error('strict', codecs.ignore_errors)
TABLE_NAME = 'test'
SINGLE_COLUMN_NAME = 'test_col'


class TestGCSOutput(unittest.TestCase):
    def setUp(self):
        self.testing_tempdir = tempfile.mkdtemp()
        self.addCleanup(
            shutil.rmtree,
            self.testing_tempdir,
        )

    def get_output_uris(self):
        output_files_patterns = self.get_files_patterns()
        return [pattern.format(self.testing_tempdir)
                for pattern in output_files_patterns]

    def get_files_patterns(self):
        return ['{}/{}*'.format(
            self.testing_tempdir,
            TABLE_NAME
        )]

    def get_second_column_name(self):
        return 'second_col'

    def create_empty_file_with_column(self):
        path = self.get_output_uris()[0]
       
