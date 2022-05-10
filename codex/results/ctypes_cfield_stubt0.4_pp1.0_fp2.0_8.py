import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(S.x), ctypes.CField)

    def test_getattr(self):
        self.assertEqual(S.x.__name__, "x")
        self.assertEqual(S.x.__doc__, "")
        self.assertEqual(S.x.__module__, __name__)
        self.assertEqual(S.x.__class__, ctypes.CField)

    def test_setattr(self):
        self.assertRaises(AttributeError, setattr, S.x, "__name__", "y")
        self.assertRaises(AttributeError, setattr, S.x, "__doc__", "y")
        self.assertRaises(AttributeError, setattr, S.x, "__module__", "y")
        self.assertRaises(AttributeError, setattr, S.x, "__class__", "y")

    def test_delattr(self):

