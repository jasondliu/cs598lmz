import io
# Test io.RawIOBase
import io
import sys
import unittest


class RawIOBaseTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'name'))
        self.assertTrue(hasattr(io.RawIOBase, 'mode'))


class RawIOBaseSubclass(io.RawIOBase):

    def readable(self):
        return False

    def writable(self):
        return False

    def seekable(self):
        return False

    def fileno(self):
        return 0


class RawIOBaseSubclassTest(unittest.TestCase):

    def test_constructor(self):
        # Issue #15785: __init__ should not be called by the constructor
        class MyRawIOBase(RawIOBaseSubclass):
            def __init__(self, *args, **kwargs):
                raise ValueError('__init__ called')
        with self.assertRaises(TypeError):
            MyRawIOBase()

    def test_unsupportedops(self):

