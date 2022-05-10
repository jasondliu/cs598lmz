import _struct
# Test _struct.StructObject and _struct.StructError
from _struct import Struct, error as StructError
from _testcapi import keyword_only_kwargs
from _testcapi import struct_int_from_buffer
from _testcapi import struct_int_as_buffer

from test import test_support


# This is used by the tests to test Struct.format:
from struct import calcsize as saved_calcsize


# generic test class
from test_typed_structs import StructTypeTestBase


class StructObjectBase(StructTypeTestBase):

    structobj = None

    def setUp(self):
        if not self.structobj:
            raise NotImplementedError

    def test_doc(self):
        s = self.structobj(self.fmt)
        self.assertIsInstance(s.__doc__, basestring)

    def test_new_from_format(self):
        s = self.structobj(self.fmt)
        self.assertEqual(s.format, self.fmt)

    def test_new_from_template(self):
