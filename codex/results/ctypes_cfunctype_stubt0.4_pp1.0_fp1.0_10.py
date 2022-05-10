import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2(arg):
    return arg

@FUNTYPE
def fun3(arg1, arg2):
    return arg1 + arg2

@FUNTYPE
def fun4(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

@FUNTYPE
def fun5(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4

@FUNTYPE
def fun6(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

@FUNTYPE
def fun7(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

@FUNTYPE
def fun8(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7
