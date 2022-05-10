import ctypes
# Test ctypes.CFUNCTYPE
class TestCFUNCTYPE(unittest.TestCase):
    def test_CFUNCTYPE_basics(self):

        # Check that CFUNCTYPE works at all
        func = ctypes.CFUNCTYPE(ctypes.c_int)(_testfunc_p_p)
        restype = func.restype
        argtypes = func.argtypes
        self.assertEqual(func(b"1"), 49)

        # Check that CFUNCTYPE can be subclassed
        class CFUNCTYPE_subclass(ctypes.CFUNCTYPE):

            def __new__(cls, func, restype=None, argtypes=(),
                    use_errno=False, use_last_error=False):
                return ctypes.CFUNCTYPE.__new__(cls, func, restype, argtypes,
                    use_errno, use_last_error)

        class CFUNCTYPE_subclass2(ctypes.CFUNCTYPE):

            def __new__(cls, restype=
