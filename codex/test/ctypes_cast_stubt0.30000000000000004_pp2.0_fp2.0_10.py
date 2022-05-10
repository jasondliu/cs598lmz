import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

class AppTestCtypes:
    spaceconfig = dict(usemodules=['_cppyy', '_rawffi', 'itertools'])

    def setup_class(cls):
        cls.w_c_lib = cls.space.appexec([], """():
            import ctypes
            return ctypes.CDLL(ctypes.util.find_library("c"))
        """)

    def test_call_c_function(self):
        import ctypes
        c_lib = self.c_lib
        assert c_lib.abs(-1) == 1
        assert c_lib.abs(1) == 1
        raises(ctypes.ArgumentError, c_lib.abs)
        raises(ctypes.ArgumentError, c_lib.abs, 1, 2)

    def test_call_c_function_with_wrong_arguments(self):
        import ctypes
        c_lib = self.c_lib
