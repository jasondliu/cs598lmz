import ctypes
# Test ctypes.CField.from_address()

class TestCFieldFromAddress(unittest.TestCase):
    def setUp(self):
        self.s = ctypes.Structure
        self.uint_32 = ctypes.c_uint32

    def test_from_address_basic(self):
        s = self.s._fields_ = [('a', self.uint_32),
                               ('b', self.uint_32),
                               ('c', self.uint_32),
                               ('d', self.uint_32),
                               ('e', self.uint_32)]
        # The address of the first field of a structure is identical
        # to the address of the structure itself:
        p = ctypes.pointer(self.s())
        self.assertEqual(self.s.a.from_address(p), self.s.a.from_address(p.contents))

        # The offset of a field is the same as the size of the previous fields:
        self.assertEqual(ctypes.sizeof(self.s.a), ctypes.addressof(
