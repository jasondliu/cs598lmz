import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_1(self):
        self.assertRaises(TypeError, fun)


if __name__ == '__main__':
    unittest.main()
