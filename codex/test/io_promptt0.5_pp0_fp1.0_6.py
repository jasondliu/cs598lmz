import io
# Test io.RawIOBase base class implementation

import io
import unittest

class RawIOTest(unittest.TestCase):
    def test_error(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase)

# Test io.BufferedIOBase base class implementation

import io
import unittest

class BufferedIOTest(unittest.TestCase):
    def test_error(self):
        self.assertRaises(io.UnsupportedOperation, io.BufferedIOBase)

# Test io.TextIOBase base class implementation

import io
import unittest

class TextIOTest(unittest.TestCase):
    def test_error(self):
        self.assertRaises(io.UnsupportedOperation, io.TextIOBase)

# Test io.StringIO

import io
import unittest

class StringIOTest(unittest.TestCase):

    def test_closed_attr(self):
        s = io.StringIO()
        self.assertFalse(s.closed)
        s
