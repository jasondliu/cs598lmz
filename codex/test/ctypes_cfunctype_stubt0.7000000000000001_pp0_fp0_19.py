import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun called")
    return 42

fun()

fun2 = FUNTYPE(fun)
fun2()

@FUNTYPE
def fun_err():
    print("error function")
    raise RuntimeError("you should never see this")

fun_err()

import sys
sys.getrefcount(1)

