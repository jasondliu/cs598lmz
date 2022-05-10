import io
# Test io.RawIOBase for issue #17893

try:
    io.RawIOBase
    import socket
    import _testcapi
    try:
        import threading
    except ImportError:
        threading = None
except ImportError:
    import sys
    sys.exit(0)

import test.test_support
import unittest


class MockSocket(io.RawIOBase):
    def __init__(self):
        pass

    def close(self):
        pass

    def fileno(self):
        return -1

class BadSocket:
    pass

class BadFileIO(io.FileIO):
    def fileno(self):
        return 'spam'

class TestRawIO(unittest.TestCase):

    def setUp(self):
        self.testfn = test.test_support.TESTFN
        self.f = open(self.testfn, 'wb')

    def tearDown(self):
        self.f.close()
        test.test_support.unlink(self.testfn)

    @unittest.skip
