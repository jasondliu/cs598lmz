import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@jit(funwrap=True)
def funwrap():
    return 1

@jit(funwrap=True)
def funwrap2(x):
    return x

@jit(argtypes=[int32])
def test_int32(x):
    return x

@jit(argtypes=[uint32])
def test_uint32(x):
    return x

@jit(argtypes=[int8])
def test_int8(x):
    return x

@jit(argtypes=[uint8])
def test_uint8(x):
    return x

@jit(argtypes=[int16])
def test_int16(x):
    return x

@jit(argtypes=[uint16])
def test_uint16(x):
    return x

def test_funwrap():
    assert funwrap() == 1
    assert call_pure_function(funwrap)() == 1

def test_funwrap2():
    assert funwrap2(1) == 1
    assert call_pure_function(funwrap2)(1) ==
