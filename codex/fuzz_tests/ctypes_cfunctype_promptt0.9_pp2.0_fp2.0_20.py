import ctypes
# Test ctypes.CFUNCTYPE()


@expectedFailurePypy
def test_CFUNCTYPE0(lib):
    @CFUNCTYPE(c_int)
    def func():
        return 42

    check(lib.int_func, func)


@expectedFailurePypy
def test_CFUNCTYPE1(lib):
    @CFUNCTYPE(c_int, c_int)
    def func(a):
        return a + 1

    check(lib.int_func, func)


@cfunc(INT)
def args(a):
    return a.value


@expectedFailurePypy
def test_CFUNCTYPE2(lib):
    @CFUNCTYPE(c_int, c_int, c_int)
    def func(a, b):
        return a + b

    check(args, func)


@expectedFailurePypy
def test_CFUNCTYPE3(lib):
    @CFUNCTYPE(c_int, c_int, c_int, c_int)
    def func(
