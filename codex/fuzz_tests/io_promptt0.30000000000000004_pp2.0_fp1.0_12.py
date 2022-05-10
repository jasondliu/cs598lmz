import io
# Test io.RawIOBase
import io
import unittest
import unittest.mock

import pytest

from test import support
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure

class RawIOTestCase(unittest.TestCase):

    def test_read(self):
        # Issue #7995: calling RawIOBase.read() should raise OSError
        r = io.RawIOBase()
        self.assertRaises(OSError, r.read)

    def test_readinto(self):
        # Issue #7995: calling RawIOBase.readinto() should raise OSError
        r = io.RawIOBase()
        self.assertRaises(OSError, r.readinto, bytearray())

    def test_readall(self):
        # Issue #7995: calling RawIOBase.readall() should raise OSError
        r = io.RawIOBase()
        self.assertRaises(OSError, r.readall)

    def
