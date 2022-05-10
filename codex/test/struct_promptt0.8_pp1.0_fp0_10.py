import _struct
# Test _struct.Struct
import unittest
import io
from unittest import mock
from test import support
# Issue 7202
from _struct import _clearcache


class StructTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.struct = _struct.Struct
        cls.fs = cls.struct('>f')
        cls.bs = cls.struct('<f')
        cls.is_64_bit = support.CPYTHON_64BIT

    def test_unpack(self):
        self._test_unpack(self.fs, 42.0)
        self._test_unpack(self.fs, -42.0)
        self._test_unpack(self.fs, 0.0)
        self._test_unpack(self.fs, 1e200)
        self._test_unpack(self.fs, -1e200)
        self._test_unpack(self.fs, 1e-200)
