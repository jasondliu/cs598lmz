import ctypes
# Test ctypes.CField()
import _ctypes_test

try:
    import _ctypes_test
except ImportError:
    import unittest
    raise unittest.SkipTest("_ctypes_test not built")

try:
    ctypes.CField
except AttributeError:
    import unittest
    raise unittest.SkipTest("requires CField")

class CMemberFuncPtrTestCase(unittest.TestCase):
    def test_call(self):
        # Check that the address of the function is stored in the pointer
        # object.
        CMP = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(_ctypes_test.get_callfunc_trampoline(CMP),
                         CMP._ptr._obj)

    def test_call_int(self):
        # Check that the address of the function is stored in the pointer
        # object.
        CMP = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
       
