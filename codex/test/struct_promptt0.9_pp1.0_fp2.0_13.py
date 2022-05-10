import _struct
# Test _struct.Struct by testing the struct module itself

from test import support
import struct
import unittest
from unittest import TestCase
import sys

class TestStruct(TestCase):
    def setUp(self):
        self.b = bytes()
        self.i4 = 0
        self.i2 = 0
        self.i1 = 0
        self.f  = 0.0
        self.all = self.b, self.i4, self.i2, self.i1, self.f

    def tearDown(self):
        pass

    def test_unpack(self):
        get = self.s.unpack
        # self.all will normally be (b'0', 0, 0, 0, 0.0), but we need to do
        # this dance because in Python 2 (b'0') != '0' and u'0' != '0'
        all = [a if type(a) != str else bytes(a, 'latin1')
               for a in self.all]
