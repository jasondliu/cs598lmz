import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return -1


def main():
    ctxt = ffi.new("struct context*", {'fun': fun})
    ctxt2 = _C.run(ctxt)
    assert ffi.string(ctxt.obuf, ctxt.olen) == 'hello world'
    assert ctxt.fun == fun
    assert ctxt2.fun == fun
    del ctxt
    del ctxt2


def test_call_function_pointer():
    fun = ffi.cast("int(*)(int)", 21)
    assert fun(5) == 21
    assert ffi.typeof(fun) == ffi.typeof("int(*)(int)")
    fun = ffi.addressof(lib, 'printf')
    assert fun("hello %s", "world") == 6
    assert ffi.typeof(fun) == ffi.typeof("int(*)(char *)")

def test_return_function_pointer():
    fun = lib.get_printf()
    assert fun("hello %s", "world") == 6
