import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(), None)

if __name__ == "__main__":
    unittest.main()
