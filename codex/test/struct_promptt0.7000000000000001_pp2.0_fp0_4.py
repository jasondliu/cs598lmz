import _struct
# Test _struct.Struct
Struct = _struct.Struct

import array
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, Struct)
        self.assertRaises(TypeError, Struct, 'abc', 1, 2, 3)

        st = Struct('x')
        self.assertEqual(st.format, 'x')
        self.assertEqual(st.size, struct.calcsize('x'))
        self.assertEqual(st.alignment, 0)

        st = Struct('xi')
        self.assertEqual(st.format, 'xi')
        self.assertEqual(st.size, struct.calcsize('xi'))
        self.assertEqual(st.alignment, struct.calcsize('i'))

    def test_unpack(self):
        st = Struct('i')
        self.assertRaises(TypeError, st.unpack)
