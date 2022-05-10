import ctypes
# Test ctypes.CField and ctypes.Field

import _testcapi

import unittest
from test import test_support


class TestCStructFields(unittest.TestCase):
    def setUp(self):
        self.p = _testcapi.new_with_struct()
        self.s = _testcapi.new_with_struct()

    def tearDown(self):
        _testcapi.delete_with_struct(self.p, self.s)

    def check(self, names):
        for name in names:
            self.assertEqual(getattr(self.p, name), getattr(self.s, name))

    def test_fields(self):
        self.check("c d g h i j k l m n r s t u v w x y z aa ab ac ad ae af".split())

    def test_fieldoffset(self):
        self.assertEqual(_testcapi.WITH_STRUCT.c.offset, 0)
        self.assertEqual(_testcapi.WITH_STRUCT.d.offset, 1)

