import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'rb')
        except FileNotFoundError:
            raise

class FileSystem:
    def __init__(self):
        self.files = []

    def touch(self, filename):
        self.files.append(File(filename))
</code>
And the test:
<code>import unittest
from unittest.mock import patch, call

from filesystem import File, FileSystem

class TestFile(unittest.TestCase):
    def test_file_not_found_error(self):
        with patch('filesystem.open') as mock_open:
            mock_open.side_effect = FileNotFoundError

            with self.assertRaises(FileNotFoundError):
                File('foo.txt')

            mock_open.assert_called_once_with('foo.txt', 'rb')

class TestFileSystem(unittest.TestCase):
    def test_touch(self):
        with patch('files
