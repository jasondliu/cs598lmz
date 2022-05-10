import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
f = fun()

# Y is not a CFUNCTYPE
class Y(int):
    def __init__(self, value):
        self.value = value
if hasattr(ctypes, 'pythonapi'):
    c_fun = ctypes.pythonapi.PyCFuncPtr(42, ctypes.c_void_p)
    c_fun.restype = Y
    c_fun.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int]

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(fun.restype is ctypes.py_object)
        self.assertTrue(fun.argtypes is None)
        self.assertEqual(fun(2), 1)

    def test_bitwidth(self):
        self.assertRaises(TypeError, ctypes.pythonapi.PyCFuncPtr, 42, 42)
        self.assertRaises(TypeError, c
