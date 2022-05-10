import codecs
# Test codecs.register_error
import os
import sys
import unittest
import warnings
from io import BytesIO, StringIO
from test import support
from test.support import TESTFN, check_warnings
from test.support.script_helper import assert_python_ok

try:
    import _testcapi
except ImportError:
    _testcapi = None

# Base class for all the codec map tests
class CodecMapTest(unittest.TestCase):
    encoding = 'undefined'

    # On Windows, the stream should be opened in binary mode to
    # avoid line-end translation, which would corrupt the test case.
    def open(self, filename, mode='rb'):
        return open(filename, mode)

    def setUp(self):
        self.filename = TESTFN + "." + self.encoding
        f = self.open(self.filename, 'w')
        f.write(self.text)
        f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_streams(self):
        f
