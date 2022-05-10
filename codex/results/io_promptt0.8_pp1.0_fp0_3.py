import io
# Test io.RawIOBase.
from test.support import run_unittest, import_module
import unittest

RawIOBase = import_module('io').RawIOBase

class MyRawIO(RawIOBase):
    def __init__(self):
        self.exception = None
        self.closed = False

    def read(self, size=-1):
        if self.exception:
            raise self.exception
        return b'x'

    def write(self, b):
        if self.exception:
            raise self.exception
        return len(b)

    def close(self):
        self.closed = True

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return True


class AutoFileTests(unittest.TestCase):
    def setUp(self):
        self.f = MyRawIO()
        self.f.name = "<MyRawIO>"

    def test_methods(self):
        self.assertEqual(self.f.readable(), True
