import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.c_long, ctypes.c_char)
f = _FFI.callback(FUNTYPE, f)

@_FFI.callback("int (PyObject *, long, char)")
def f2(o, l, c):
    return 0

f2(None, 1, b'1')

@_FFI.callback("int (*)(PyObject *, long, char)")
def f3():
    return f2

f3()(None, 1, b'1')

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long)
@_FFI.callback("long (*)(long)")
def f4():
    @FUNTYPE
    def g(x):
        return x + 1
    return g

f4()(2)

@_FFI.callback("long (*)(long)")
def f5(x):
    return x + 1
f5(3)

_FFI.callback("long (*)(long)", f
