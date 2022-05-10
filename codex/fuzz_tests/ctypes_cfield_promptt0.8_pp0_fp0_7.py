import ctypes
# Test ctypes.CField
import ctypes.test.test_cf

# try to get the external function 'get_errno' which may not
# be available on all platforms, in which case we substitute
# a dummy function.
try:
    extern_func = ctypes.CDLL(None).get_errno
except AttributeError:
    # assume we're on Windows
    extern_func = None
except OSError:
    extern_func = None

if extern_func:
    class CFuncPtr_Test(unittest.TestCase):
        def test_errno(self):
            global extern_func
            self.assertEqual(0, extern_func())

        def test_restype(self):
            global extern_func
            extern_func.restype = ctypes.c_int
            self.assertEqual(0, extern_func())

        def test_argtypes(self):
            global extern_func
            extern_func.argtypes = (ctypes.c_int,)
            self.assertEqual(0, ex
