import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class _T(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(_T._fields_, [("a", ctypes.c_int)])
        self.assertEqual(_T._field_types_, {'a': ctypes.c_int})

    def test_dup_name(self):
        class _T(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("a", ctypes.c_int)]

        self.assertEqual(_T._fields_, [("a", ctypes.c_int)])
        self.assertEqual(_T._field_types_, {'a': ctypes.c_int})

    def test_dup_name2(self):
        # like the test above, but the "duplicate" member is
        # a nested structure.
        class _T(ctypes.Structure):
