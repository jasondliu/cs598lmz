import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    # Sanity check
    def test_field_sanity(self):
        c_field = ctypes.CField()
        c_field.lname = 'lname'
        c_field.length = 8
        c_field.fldtype = 'float64'
        c_field.dtype = getattr(np, c_field.fldtype)
        self.assertEqual(c_field.lname, 'lname')
        self.assertEqual(c_field.length, 8)
        self.assertEqual(c_field.fldtype, 'float64')
        
        self.assertEqual(c_field.dtype, np.float64)

        for i in range(4):
            with self.subTest(i=i):
                c_copy = c_field.copy
                c_copy.dtype = np.float32
                self.assertFalse(c_copy.dtype == c_field.dtype)

        self.assertEqual(c_copy.
