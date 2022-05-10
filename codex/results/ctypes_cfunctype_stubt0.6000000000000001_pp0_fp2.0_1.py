import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):

    def test_PyObject_Call(self):
        self.assertRaises(TypeError, ctypes.pythonapi.PyObject_Call, fun, None, None)

if __name__ == "__main__":
    unittest.main()
