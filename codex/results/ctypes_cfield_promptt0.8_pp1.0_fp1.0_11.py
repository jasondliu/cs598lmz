import ctypes
# Test ctypes.CField
class FixedTest(unittest.TestCase):
    def test_from(self):
        self.assertEqual(ctypes.__version__, __version__)
        tp = ctypes.c_int
        self.assertTrue(tp._length_ is 4)
        self.assertTrue(tp._alignment_ is 4)
        for bf in ['c', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L']:
            tp = ctypes.c_byte(bf)
            self.assertTrue(tp._length_ is 1)
            self.assertTrue(tp._alignment_ is 1)
        for bf in ['f', 'd']:
            tp = ctypes.c_float(bf)
            self.assertTrue(tp._length_ is 8)
            self.assertTrue(tp._alignment_ is 8)
        for bf in ['f', 'd']:
            tp = ctypes.c_float(bf)
            self.assertTrue(tp._length_ is 8)
           
