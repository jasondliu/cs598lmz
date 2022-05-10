import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class Test(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(), 42)

    def test_fun_callable(self):
        self.assertEqual(fun(), 42)

if __name__=='__main__':
    unittest.main()
""")

    def test_fun_callable(self):
        self.assertEqual(self.fun(), 42)

if __name__=='__main__':
    unittest.main()
