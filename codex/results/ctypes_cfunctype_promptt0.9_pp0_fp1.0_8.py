import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE1 = ctypes.CFUNCTYPE(ctypes.c_int)
CFUNCTYPE1(lambda : 0)
# Test ctypes.PyCFuncPtr
class PyCFuncPtrTestCase(unittest.TestCase):

    def test_issue2680(self):
        # PyCFuncPtr should raise an exception when
        # used as dllfunction instead of c_void_p.
        self.assertRaises(TypeError, WinDLL, None)

    def test_CFuncPtr(self):
        if os.name == "nt":
            # Only one functype per return type can exist, so we
            # have to keep track of alrady defined ones.
            dllfunc_cache = {}
            for restype in [c_int, c_long, c_double, c_char_p]:
                func = CDLL(_ctypes_test.__file__)._testfunc_p_p

                # First try: simple decimal
                dllfunc = CFUNCTYPE(restype, c_void_p
