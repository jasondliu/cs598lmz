import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):

    def test_fun(self):
        self.assertEqual(fun(), None)

    def test_fun_return_none(self):
        self.assertEqual(fun.return_none(), None)

    def test_fun_return_none_with_int(self):
        self.assertEqual(fun.return_none(1), None)

    def test_fun_return_none_with_int_and_int(self):
        self.assertEqual(fun.return_none(1, 2), None)

    def test_fun_return_none_with_int_and_int_and_int(self):
        self.assertEqual(fun.return_none(1, 2, 3), None)

    def test_fun_return_none_with_int_and_int_and_int_and_int(self):
        self.assertEqual(fun.return_none(1, 2, 3, 4), None)

    def test_fun_return_none_with_int
