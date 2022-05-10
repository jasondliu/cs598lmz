import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fun(), None)

    def test_2(self):
        self.assertEqual(fun(), None)

if __name__ == "__main__":
    unittest.main()
