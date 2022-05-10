import ctypes
# Test ctypes.CFUNCTYPE
def py_callback(x):
    return x*2

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_callback(lib, func, restype, argtypes):
    cb = CMPFUNC(py_callback)
    res = func(42, cb)
    assert res == 84

def test_callbacks():
    for name, (restype, argtypes, errcheck) in FUNCTIONS.items():
        yield test_callback, name, restype, argtypes

def test_CFUNCTYPE_cache():
    # test that the cache of callbacks is working
    # this used to crash with a segfault
    for i in range(100):
        cb = CMPFUNC(py_callback)
        assert cb(i) == i*2

def test_void_p():
    from ctypes import c_void_p
    # A void * pointer can be used as an int
