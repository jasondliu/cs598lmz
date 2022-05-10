import _struct
# Test _struct.Struct.__getitem__
from test import test_support
import unittest


class StructTest(unittest.TestCase):

    def test_getitem(self):
        st = _struct.Struct('i')
        self.assertEqual(st[0], 0)
        self.assertEqual(st[1], 4)
        self.assertEqual(st[2], 8)
        self.assertEqual(st[-1], 8)
        self.assertEqual(st[-2], 4)

    def test_unpack_from(self):
        st = _struct.Struct('i')
        self.assertEqual(st.unpack_from('\0' * 4, 0), (0,))
        self.assertEqual(st.unpack_from('\0' * 4, 1), (0,))
        self.assertEqual(st.unpack_from('\0' * 4, 2), (0,))
        self.assertEqual(st.unpack_from('\0' * 4, 3), (0,))

   
