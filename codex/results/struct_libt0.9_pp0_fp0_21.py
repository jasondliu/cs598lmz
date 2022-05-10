import _struct
import sys
import tempfile
import unittest

from test import support


class StructTestCase(unittest.TestCase):

    def tearDown(self):
        support.gc_collect()
        support.reap_children()

    # Issue #10859.
    def test_bogus_kwargs(self):
        self.assertRaises(TypeError, _struct.Struct, 'i', i=1)
        self.assertRaises(TypeError, _struct.Struct, 'i', format=1)

    # Issue #11829.
    def test_readonly_attributes(self):
        st = _struct.Struct('i')
        self.assertRaises(AttributeError, setattr, st, 'format', 'p')
        self.assertRaises(AttributeError, setattr, st, 'size', 'p')

    def test_structobject(self):
        types = [('h', 'short', 'int'),
                 ('i', 'int', 'int'),
                 ('l', 'long', 'long'),
                 ('q', 'longlong
