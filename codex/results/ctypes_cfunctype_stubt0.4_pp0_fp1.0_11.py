import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):

    def test_py_object(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_2(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_3(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_4(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_5(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_6(self):
        self.assertEqual(fun(), None)
        self.assertEqual(fun(), None)

    def test_py_object_7(self):
        self.assertEqual
