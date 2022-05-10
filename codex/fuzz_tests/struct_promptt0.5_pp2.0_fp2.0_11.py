import _struct
# Test _struct.Struct

import unittest
import sys

class StructTest(unittest.TestCase):

    def test_struct_doc_example(self):
        # From the struct.Struct docstring
        import struct
        import binascii
        s = struct.Struct('i?f')
        packed_data = s.pack(12345, False, -3.14)
        print('Original values:', (12345, False, -3.14))
        print('Format string  :', s.format)
        print('Uses           :', s.size, 'bytes')
        print('Packed Value   :', binascii.hexlify(packed_data))
        print('Unpacked Value :', s.unpack(packed_data))

    def test_unpack(self):
        # Test unpacking of various struct formats
        import binascii
        s = _struct.Struct('hi')
        packed_data = s.pack(12345, 67890)
        unpacked_data = s.unpack(packed_data)
        self.assertEqual(
