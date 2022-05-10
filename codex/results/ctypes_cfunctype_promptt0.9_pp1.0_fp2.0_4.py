import ctypes
# Test ctypes.CFUNCTYPE
try:
    from lib.cppyy import gbl
    from lib.cppyy import _cppyy as cppyy
    import _multiprocessing
except ImportError:
    raise ImportError("Test requires CPython >= 2.7.")

pylong = int

cp = cppyy.gbl # for convenience

class CMiscTestCtypes:
    """Test callback functions based on ctypes, as well as STDCALL/CDECL callback wrappers"""

    def setup_method(self, method):
        self.cfunc_cb_int_i        = cppyy.gbl.cfunc_cb_int_i
        self.cfunc_cb_int_d        = cppyy.gbl.cfunc_cb_int_d
        self.cfunc_cb_long_l       = cppyy.gbl.cfunc_cb_long_l
        self.cfunc_cb_ulong_ul     = cppyy.gbl.cfunc_cb_ulong_ul
        self.cfunc_cb_llong_
