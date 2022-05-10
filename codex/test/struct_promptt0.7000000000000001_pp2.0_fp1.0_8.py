import _struct
# Test _struct.Struct

import test.test_support as support

class SizesTestCase(unittest.TestCase):
    def setUp(self):
        self.s = _struct.Struct('i')

    def test_size(self):
        self.assertEqual(self.s.size, 4)

    def test_alignment(self):
        self.assertEqual(self.s.alignment, 4)

    def test_pack_into_buffer(self):
        import array
        for typecode in 'bhil':
            b = array.array(typecode, [0, 1, 2, 3, 4, 5, 6, 7])
            self.s.pack_into(b, 2, 42)
            self.assertEqual(b, array.array(typecode, [0, 1, 42, 3, 4, 5, 6, 7]))

class PackTestCase(unittest.TestCase):
    def setUp(self):
        self.s = _struct.Struct('i')

