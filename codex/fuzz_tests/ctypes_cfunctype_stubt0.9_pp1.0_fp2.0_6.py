import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

fun.func_name = None

class GetNameTests(unittest.TestCase):
    def test_name(self):
        self.assertTrue(nameof(fun) is None)
        self.assertTrue(nameof(fun.__code__) is None)

if __name__ == '__main__':
    unittest.main()
