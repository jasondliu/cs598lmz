import mmap
# Test mmap.mmap()
import os
# Test os.stat() and os.path.getsize()
import tempfile
# Test tempfile.TemporaryFile()
import unittest
# Test unittest.TestCase.assertEqual()

# Test that mmap(MAP_PRIVATE) works correctly by using it to copy a file.
class TestCopyFile(unittest.TestCase):
    def setUp(self):
        self.in_file = tempfile.TemporaryFile()
        self.out_file = tempfile.TemporaryFile()
        self.in_file.write(b"Hello World")
        self.in_file.flush()

    def test_copy_file(self):
        in_file = self.in_file
        out_file = self.out_file
        in_file.seek(0)
        in_map = mmap.mmap(in_file.fileno(), 0, access=mmap.ACCESS_READ)
