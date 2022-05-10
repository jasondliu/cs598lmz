import ctypes
# Test ctypes.CField()

class TestCField(unittest.TestCase):
    def test_basic(self):
        class C(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField),
            ]
        self.assertEqual(C._fields_, [
            ("a", ctypes.CField),
            ("b", ctypes.CField),
            ("c", ctypes.CField),
        ])
        self.assertEqual(C._pack_, 1)

    def test_pack(self):
        class C(ctypes.Structure):
            _pack_ = 2
            _fields_ = [
                ("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField),
            ]
        self.assertEqual(C._fields_, [
            ("a", ctypes.CField),
            ("b", ctypes.CField),
            ("c", ctypes
