import _struct
# Test _struct.Struct
import struct
# Test struct.Struct
import unittest
# Test unittest.main()
import sys
# Test sys.exit()
import os
# Test os.path.isfile()
import io
# Test io.StringIO()

class TestStruct(unittest.TestCase):
    def test_Struct(self):
        # Test _struct.Struct
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(_struct.Struct('i').pack(1)), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00'), (1,))
        self.assertEqual(_struct.Struct('i').unpack(b
