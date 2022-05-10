import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(isinstance(fun, FUNTYPE))
        self.assertRaises(TypeError, FUNTYPE, fun)
        self.assertRaises(TypeError, FUNTYPE, 123)
        self.assertRaises(TypeError, FUNTYPE, 123, 456)
        self.assertRaises(TypeError, FUNTYPE, 123, 456, 789)
        self.assertRaises(TypeError, FUNTYPE, 123, 456, 789, 101112)
        self.assertRaises(TypeError, FUNTYPE, 123, 456, 789, 101112, 131415)
        self.assertRaises(TypeError, FUNTYPE, 123, 456, 789, 101112, 131415,
                          161718)

    def test_call(self):
        self.assertEqual(fun(), None)
        self.assertRaises(TypeError, fun, 1)
        self.assertRaises(TypeError, fun, 1, 2)
