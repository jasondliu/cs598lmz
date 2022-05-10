import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double
    z = ctypes.c_short
    i = ctypes.c_int
    j = ctypes.c_int

class test_types(BaseTestChecker):

    def test_float_to_int(self):
        self.ffi.cdef("typedef long long myint_t;")
        r = self.ffi.cast("myint_t", 2.5)
        assert r == 2
        r = self.ffi.cast("myint_t", 2.51)
        assert r == 3
        r = self.ffi.cast("myint_t", 12345678.0)
        assert r == 12345678
        r = self.ffi.cast("myint_t", -1.23)
        assert r == -1
        self.lib.cast_test(2.5, -1.23, 12345678.0)

    def test_float_to_float(self):
        self.ffi.cdef("typedef double
