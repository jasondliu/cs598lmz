import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def fun2():
    return "fun2"


class TestCtypeMethodCall(unittest.TestCase):
    """ Test calling ctypes methods.
    """
    def test_call_c_method(self):
        """ Test calling a ctypes function.
        """
        _test_call_c_method(self, fun)

    def test_call_c_method2(self):
        """ Test calling a ctypes function.
        """
        _test_call_c_method(self, fun2)


if __name__ == '__main__':
    unittest.main()
