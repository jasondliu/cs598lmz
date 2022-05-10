import io
# Test io.RawIOBase

import os
import socket
import subprocess
import sys

from test import support
from test.support import run_unittest


class MockRawIOBase(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def close(self):
        pass

class MockUnseekableIOBase(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return False

    def close(self):
        pass


class RawIOBaseTest(unittest.TestCase):

    def test_overflow(self):
        self.assertEqual(self.mock.readinto(b""), 0)
        self.assertEqual(self.mock.write(b""), None)


class RawIOBaseDuplexTest(RawIOBaseTest):

    def setUp(self):
        self.mock = MockRawIOBase()


