import codecs
# Test codecs.register_error('myerror', myerror)

import sys
import unittest
from test import support

# We need to make sure sys.stdin, sys.stdout and sys.stderr are TextIO
# instances, so we'll use StringIO instances to replace them.

class TextIOWrapperTest(unittest.TestCase):

    def setUp(self):
        self.sys_stdin = sys.stdin
        self.sys_stdout = sys.stdout
        self.sys_stderr = sys.stderr
        self.string_stream = support.StringIO
        sys.stdin = self.string_stream("")
        sys.stdout = self.string_stream("")
        sys.stderr = self.string_stream("")

    def tearDown(self):
        sys.stdin = self.sys_stdin
        sys.stdout = self.sys_stdout
        sys.stderr = self.sys_stderr

    def test_attributes(self):
        f = io.TextIOWrapper(self
