import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_double)]

class Test(unittest.TestCase):
    def test_override_fields(self):
        self.assertEqual(S.x, ctypes.c_int)
        self.assertEqual(S.y, ctypes.c_double)

    def test_override_field_names(self):
        self.assertEqual(S._fields_[0], ('x', ctypes.c_int))
        self.assertEqual(S._fields_[1], ('y', ctypes.c_double))

    def test_override_field_names_and_values(self):
        # this crashes python if _fields_ is overridden first
        self.assertEqual((S.x, S.y), (ctypes.c_int, ctypes.c_double))


if __name__ == '__main__':
    unittest.main()
