import _struct
# Test _struct.Struct

import unittest

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        import _struct
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(_struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'abcdef', 3), (11259375,))
        self.assertEqual(_struct.Struct('i').unpack_from(b'abcdef', 3, 1), (11259375,))
        self.assertEqual(_struct.Struct('i').unpack_from(memoryview(b'abcdef'), 3), (11259375,))
        self.assertEqual(_struct.Struct('i').unpack_from(memoryview(b'abcdef'), 3, 1
