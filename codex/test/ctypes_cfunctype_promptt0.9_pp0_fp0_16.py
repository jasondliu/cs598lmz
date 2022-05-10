import ctypes
# Test ctypes.CFUNCTYPE on required arg types

MAXSIZE = 10

def test(fun):
    if fun(1) != 1:
        raise RuntimeError
    if fun(1026) != 1026:
        raise RuntimeError
    if fun(1000) != 1000:
        raise RuntimeError
    if fun(-100) != -100:
        raise RuntimeError
    if fun(100000000000) != 100000000000:
        raise RuntimeError
    for i in range(MAXSIZE):
        s = 0x7FFF0000 | i
        if fun(s) != s:
            raise RuntimeError

F1 = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint)
F2 = ctypes.CFUNCTYPE(ctypes.c_ushort, ctypes.c_uint)
F3 = ctypes.CFUNCTYPE(ctypes.c_short, ctypes.c_uint)

fun1 = F1(lambda x: x)
fun2 = F2(lambda x: x)
