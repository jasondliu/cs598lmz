import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2

def get_cfun(name, lib):
    return FUNTYPE(getattr(lib, name))

class Test(unittest.TestCase):
    def test_call_fun(self):
        self.assertEqual(fun(), 2)

    def test_call_cfun(self):
        lib = ctypes.CDLL(libtest.__file__)
        cfun = get_cfun('fun', lib)
        self.assertEqual(cfun(), 2)
