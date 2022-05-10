import ctypes
# Test ctypes.CField:

class TestCField(unittest.TestCase):

    def test_bitfields(self):
        class BitFields(ctypes.Structure):
            _fields_ = [
                    ("x", ctypes.c_int16, 2),
                    ("y", ctypes.c_int16, 3),
                    ("z", ctypes.c_int16, 16),
                    ]
        x = BitFields()
        x.x = 3
        x.y = 7
        x.z = -1
        self.assertEqual(x.x, 3)
        self.assertEqual(x.y, 7)
        self.assertEqual(x.z, -1)
        #
        x.z = 65535
        self.assertEqual(x.x, 3)
        self.assertEqual(x.y, 7)
        self.assertEqual(x.z, -1)
        #
        x.z = 0x1ffff
        self.assertEqual(x.x, 3)
        self.assertEqual(x
