import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(), None)

    def test_fun_args(self):
        self.assertEqual(fun(1, 2), None)

    def test_fun_kwargs(self):
        self.assertEqual(fun(a=1, b=2), None)

if __name__ == "__main__":
    unittest.main()
