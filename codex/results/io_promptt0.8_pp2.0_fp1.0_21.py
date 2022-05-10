import io
# Test io.RawIOBase
import tempfile
import unittest

from test import support
from test.support import _2G

# MS-Windows requires a file to be opened in binary mode to return
# the correct value for file.mode (other platforms always use 'r').
tmpnam = tempfile.mktemp()
with open(tmpnam, 'wb') as f:
    f.write(b'a' * 100)


def make_tests(cls):
    class Mixin:
        cls = cls

        def setUp(self):
            # XXX(nnorwitz): this should be a context manager, but that
            # means either the tests need to be rewritten or we need
            # to implement __exit__ for all subclasses.  Better to use
            # the context manager to cleanup the new RawIOBase files.
            self.rawio = self.cls()

        def test_constructor(self):
            # Check that the constructor raises IOError for invalid modes.
            self.assertRaises(IOError, self.cls, "")
            self.assertRaises(IOError, self
