import _struct
# Test _struct.Struct
import unittest
from test import support
from test.support import BigaddrspaceTestCase

class StructTestCase(unittest.TestCase):

    def test_big_endian_format(self):
        # test that big endian format characters are accepted
        # (exercise the converter code)
        _struct.Struct('>i')
        _struct.Struct('>h')
        _struct.Struct('>l')
        _struct.Struct('>q')
        _struct.Struct('>f')
        _struct.Struct('>d')

    def test_native_size(self):
        # test that native size format characters are accepted
        _struct.Struct('@i')
        _struct.Struct('@h')
        _struct.Struct('@l')
        _struct.Struct('@q')
        _struct.Struct('@f')
        _struct.Struct('@d')

    def test_native_format(self):
        # test that native format characters are accepted
        _struct.Struct('=i')
        _struct.Struct('=h')
       
