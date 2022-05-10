import io
# Test io.RawIOBase

import io
import sys
import unittest
from test import support
from test.support import bigmemtest, TESTFN, unlink
import warnings

class RawIOBaseTest:
    # Additional constructor tests

    def test_constructor(self):
        self.assertRaises(ValueError, self.raw.__init__, '', 0, -1)
        self.assertRaises(ValueError, self.raw.__init__, '', -1, 0)

    def test_default_constructor(self):
        del self.raw.raw
        self.assertRaises(TypeError, self.raw)

    def test_constructor_bad_args(self):
        self.assertRaises(TypeError, self.raw.__init__, 0, 0)
        self.assertRaises(TypeError, self.raw.__init__, 0, '0')
        self.assertRaises(TypeError, self.raw.__init__, 0, 0, 0)
        self.assertRaises(TypeError, self.raw.__init__, 0, '0
