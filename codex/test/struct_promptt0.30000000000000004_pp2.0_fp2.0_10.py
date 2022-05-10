import _struct
# Test _struct.Struct

import struct
import sys
import unittest

import test.support

class StructTestCase(unittest.TestCase):

    def test_struct_doc_example(self):
        # Example given in the module doc string.
        import _struct
        s = _struct.Struct('i?f')
        packed = s.pack(12345, False, 3.14159)
        unpacked = s.unpack(packed)
        self.assertEqual(unpacked, (12345, False, 3.14159))

    def test_struct_error_message(self):
        # Test error messages for struct module.
        self.assertRaisesRegex(struct.error,
                               'bad char in struct format',
                               struct.Struct, 'Z')
        self.assertRaisesRegex(struct.error,
                               'bad char in struct format',
                               struct.Struct, 'Zi')
        self.assertRaisesRegex(struct.error,
                               'bad char in struct format',
                               struct.Struct, '=Zi')
       
