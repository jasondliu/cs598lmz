import mmap
import os
import shutil
import tempfile
import unittest

from retrace import ArchiveParser, _ArchiveParser
from retrace.tests import get_fixture


class TestArchiveParser(unittest.TestCase):
    def test_log_path_with_offset(self):
        ap = _ArchiveParser(
            get_fixture('coredump.tar.xz'),
            get_fixture('coredump.map'),
            get_fixture('coredump.log'),
            0, None)
        self.assertEqual(ap.log_path, get_fixture('coredump.log'))

    def test_log_path_with_in_memory_file(self):
        log_name = os.path.join(os.path.dirname(__file__), 'coredump.log')
        with open(log_name, 'rb') as log_file, tempfile.NamedTemporaryFile() as temp_file:
            temp_file.write(log_file.read())
            temp_file.flush()
