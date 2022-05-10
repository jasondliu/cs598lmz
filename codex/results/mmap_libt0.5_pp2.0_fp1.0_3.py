import mmap
import os.path
import re
import sys
import tempfile
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def assertIn(self, member, container, msg=None):
        if sys.version_info[0] == 3:
            return super().assertIn(member, container, msg)
        else:
            return self.assertTrue(member in container, msg)

    def assertNotIn(self, member, container, msg=None):
        if sys.version_info[0] == 3:
            return super().assertNotIn(member, container, msg)
        else:
            return self.assertFalse(member in container, msg)

    def assertRegex(self, text, regex, msg=None):
        if sys.version_info[0] == 3:
            return super().assertRegex(text, regex, msg)
        else:
