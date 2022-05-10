import io
class File(io.RawIOBase):
    """This is a simple example to show how to mock a class using a context
    manager for setup and teardown.
    """
    def __init__(self, filename, mode):
        self.file = open(filename, mode=mode)

    def __enter__(self):
        return self.file

    def __exit__(self, *args):
        self.file.close()


class FileTestCase(unittest.TestCase):

    @patch('File')
    def test_with_file(self, file_mock):
        """The with statement patches File for you automatically,
        but you need to configure the mock to return a mock for
        'open'.
        """
        file_mock.return_value.__enter__.return_value.read.return_value = 'This is a test'
        with File('filename', 'r'):
            assert file_mock.return_value.__enter__.return_value.read.return_value == 'This is a test'
</code>
Now the call to <code>file_mock.return
