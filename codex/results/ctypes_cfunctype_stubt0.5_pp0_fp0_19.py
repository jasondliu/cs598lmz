import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class Test(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(), 1)

if __name__ == "__main__":
    unittest.main()
