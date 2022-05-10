import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"

def test_return_type_check():
    # If the return type is not an integer, it should raise an error
    py.test.raises(TypeError, "jit.JitFunction(FUNTYPE, [])")

def test_pow():
    def pow(a, b):
        return a ** b
    jit_pow = jit.JitFunction(pow)
    assert jit_pow(2, 3) == 8
    assert jit_pow(2, 4) == 16
    assert jit_pow(2, 5) == 32
    assert jit_pow(2., 3.) == 8
    assert jit_pow(2., 4.) == 16
    assert jit_pow(2., 5.) == 32
    assert jit_pow(2., 4.) == 16
    assert jit_pow(2., 5.) == 32
    assert jit_pow(2.5, 4) == 39.0625
