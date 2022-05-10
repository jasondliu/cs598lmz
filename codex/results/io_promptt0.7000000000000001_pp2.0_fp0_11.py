import io
# Test io.RawIOBase
import os
import sys
import unittest
from test import support
from test.support import bigmemtest
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.support.script_helper import assert_python_exit_code


class TestRawIOBase(unittest.TestCase):
    """Basic tests for io.RawIOBase."""

    def test_constructor(self):
        # RawIOBase is an abstract class.
        self.assertRaises(TypeError, io.RawIOBase)

    def test_readinto(self):
        # RawIOBase.readinto() is not implemented.
        r = io.RawIOBase()
        self.assertRaises(NotImplementedError, r.readinto, bytearray(10))


class TestBufferedIOBase(unittest.TestCase):
    """Basic tests for io.BufferedIOBase."""

    def test_constructor(self):
        # RawIOBase is an abstract class.
       
