import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_cfunc():
    assert fun() == 42


def test_cfunc_with_arg():
    @FUNTYPE
    def fun2(a):
        return a
    assert fun2(42) == 42
    assert fun2(41) == 41
    raises(TypeError, fun2)


def test_cfunc_with_kwarg():
    @FUNTYPE
    def fun2(a):
        return a
    assert fun2(a=42) == 42
    assert fun2(a=41) == 41
    raises(TypeError, fun2, 42)


def test_cfunc_with_default():
    @FUNTYPE
    def fun2(a=42):
        return a
    assert fun2() == 42
    assert fun2(a=41) == 41
    raises(TypeError, fun2, 41)


def test_cfunc_with_kwdefault():
    @FUNTYPE
    def fun2(a=42):
        return a
    assert fun2() == 42
    assert fun2(a=41
