import io
# Test io.RawIOBase
from test import support
import unittest
import tempfile
from test.support.script_helper import assert_python_ok

def findfile(file, here=__file__):
    import os
    from os.path import dirname
    here = dirname(here)
    file = os.path.join(here, file)
    try:
        fp = open(file, 'rb')
    except OSError:
        return None
    with fp:
        return fp.read()


@unittest.skipUnless(findfile('code1.py'),
    'Failed to locate test file')
class CReaderTests(unittest.TestCase):

    def setUp(self):
        import os
        here = self.here = os.path.dirname(__file__)
        self.creader = io.open(os.path.join(here, 'code1.py'), 'r', 1)

    def tearDown(self):
        self.creader.close()
        del self.creader

    def test_read
