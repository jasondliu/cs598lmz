import ctypes
# Test ctypes.CFUNCTYPE

class Test(BaseCTypesTestChecker):
    def test_CFUNCTYPE(self):
        # Test a c_int returning c function
        prototype = ctypes.CFUNCTYPE(ctypes.c_int)
        result = prototype(lambda: 42)(self.fn)
        self.assertEqual(result.value, 42)

        # Test a c_int returning c function with param
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        result = prototype(lambda x: x*2)(self.fn, 21)
        self.assertEqual(result.value, 42)

        # Test a c_void_p returning c function
        prototype = ctypes.CFUNCTYPE(ctypes.c_void_p)
        result = prototype(lambda: id(self.fn) & 0xFFFFFFFF)(self.fn)
        self.assertEqual(result.value, id(self.fn) & 0xFFFFFFFF)

        # Test a c_void_p returning c function with param
