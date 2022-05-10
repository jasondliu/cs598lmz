import ctypes
# Test ctypes.CFUNCTYPE. 
# The returned object is a callable Python object which can be passed
# to callbacks.
def _test_CFUNCTYPE(self, obj):
    try:
        from ctypes import CFUNCTYPE
    except ImportError:
        raise unittest.SkipTest("ctypes not available")
    callback_func = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)
    self.assertEqual(callback_func(3), 4)


def test_main():
    support.run_unittest(test_types)
    support.run_unittest(test_functions)

if __name__ == "__main__":
    test_main()
