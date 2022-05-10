import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype():
    # This test is not complete, but it's better than nothing.
    # It should be extended to cover more cases.
    import _ctypes
    from ctypes import c_int, c_void_p, c_char_p, CFUNCTYPE
    from _ctypes import PyObj_FromPtr
    #
    # test calling a function with a CFUNCTYPE argument
    #
    def func(restype, argtypes):
        # restype and argtypes are lists of types
        # create a function with the given restype and argtypes
        # and call it
        func.called = 0
        @CFUNCTYPE(restype, *argtypes)
        def f(*args):
            func.called += 1
            func.args = args
            return args[0]
        res = f(*range(len(argtypes)))
        assert res == 0
        assert func.called == 1
        assert func.args == tuple(range(len(argtypes)))
    #
    # test calling a function with a CFUN
