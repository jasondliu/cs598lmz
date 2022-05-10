import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Array = ctypes.c_int * 2
try:
    class TestSlices(BaseTestCase):
        def test_ctypes_field(self):
            self.assertEqual(S.x.__reduce__(), (S.x, ()))

        def test_ctypes_array(self):
            self.assertEqual(ctypes.Array.__reduce__(), (ctypes.Array, ()))

        def test_ctypes_array_sequence(self):
            self.assertEqual(ctypes.Array((1, 2)).__reduce__(), (ctypes.Array, (1, 2)))

        def test_ctypes_field_getattr(self):
            self.assertEqual(S.x.meaning_of_life, 42)
except AttributeError:
    pass # ctypes doesn't exist
except TypeError:
    pass # ctypes.Structure subclasses not supported

if __name__ == "__main__":
    unittest.main()
