import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_base_class(self):
        self.assertEqual(ctypes._CData, object)
        self.assertEqual(ctypes._SimpleCData, object)

    def test_isinstance(self):
        self.assertTrue(isinstance(ctypes.c_int(), ctypes.c_int))
        self.assertTrue(isinstance(ctypes.c_int(), ctypes._CData))
        self.assertTrue(isinstance(ctypes.c_int(), object))
        self.assertTrue(isinstance(ctypes.c_int, type))
        self.assertTrue(isinstance(ctypes.c_int, ctypes.c_int))
        self.assertTrue(isinstance(ctypes.c_int, ctypes._CData))
        self.assertTrue(isinstance(ctypes.c_int, object))

        self.assertTrue(isinstance(ctypes.c_int, ctypes.c_int))
        self.assertTrue(isinstance(ctypes.c
