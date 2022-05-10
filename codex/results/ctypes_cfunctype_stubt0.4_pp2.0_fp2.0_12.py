import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42


class TestPyObj(unittest.TestCase):
    def test_py_obj(self):
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42)
        self.assertEqual(fun(), 42
