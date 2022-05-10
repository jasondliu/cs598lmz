import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase, UnsupportedOperation

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        # No constructor test needed, as abstract
        pass

    def test_read(self):
        # No read test needed, as abstract
        pass

    def test_readinto(self):
        # No readinto test needed, as abstract
        pass

    def test_write(self):
        # No write test needed, as abstract
        pass

    def test_fileno(self):
        # No fileno test needed, as abstract
        pass

    def test_readable(self):
        # No readable test needed, as abstract
        pass

    def test_writable(self):
        # No writable test needed, as abstract
        pass

    def test_seekable(self):
        # No seekable test needed, as abstract
        pass

    def test_close(self):
        # No close test needed, as abstract
        pass

    def test_isatty(self):
