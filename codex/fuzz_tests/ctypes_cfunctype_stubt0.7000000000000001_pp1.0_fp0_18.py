import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1.0

def fun2():
    return 1.0

class Callable:
    def __call__(self):
        return 1.0

fun3 = Callable()

class Test(unittest.TestCase):
    def test_from_function(self):
        f = Function(fun)
        self.assertEqual(f(), 1.0)
    def test_from_function_2(self):
        f = Function(fun2)
        self.assertEqual(f(), 1.0)
    def test_from_callable(self):
        f = Function(fun3)
        self.assertEqual(f(), 1.0)

if __name__ == '__main__':
    unittest.main()
