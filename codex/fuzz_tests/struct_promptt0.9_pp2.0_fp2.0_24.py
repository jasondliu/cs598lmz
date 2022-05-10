import _struct
# Test _struct.Struct

import sys
if sys.version_info < (3, 4):
    raise RuntimeError("_struct requires at least Python 3.4")

import struct
import unittest
import warnings

from test.test_support import (run_unittest, import_module,
                               run_with_locale,
                               swap_attr)

class StructTest(unittest.TestCase):
    def setUp(self):
        self.s = _struct.Struct("x")
        self.fmt = "<h"
        self.s2 = _struct.Struct(self.fmt)

    def test_error(self):
        for errfmt in ("xxxx", "h", "hlo"):
            self.assertRaises(struct.error, _struct.Struct, errfmt)

    def test_args(self):
        self.assertEqual(_struct.Struct("@"), _struct.Struct())
        self.assertRaises(_struct.Struct("i").error,
                          _struct.Struct("i").pack, 42, 99)
        self.assert
