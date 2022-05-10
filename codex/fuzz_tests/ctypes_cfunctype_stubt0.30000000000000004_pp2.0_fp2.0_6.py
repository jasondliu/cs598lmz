import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test(unittest.TestCase):
    def test_cfun(self):
        self.assertEqual(fun(), None)

    def test_cfun_error(self):
        with self.assertRaises(TypeError) as cm:
            @FUNTYPE
            def fun():
                return 1
        self.assertEqual(str(cm.exception),
                         "CFUNCTYPE functions must return None or a ctypes type")

    def test_cfun_error_2(self):
        with self.assertRaises(TypeError) as cm:
            @FUNTYPE
            def fun():
                return 1, 2
        self.assertEqual(str(cm.exception),
                         "CFUNCTYPE functions must return None or a ctypes type")

    def test_cfun_error_3(self):
        with self.assertRaises(TypeError) as cm:
            @FUNTYPE
            def fun():
                return 1, 2, 3
        self.assertEqual(str(cm.exception),
                         "CF
