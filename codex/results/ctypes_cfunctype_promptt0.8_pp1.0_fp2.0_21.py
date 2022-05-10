import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_double and callback

from ctypes import CFUNCTYPE, c_int, c_double

SIMPLE_FUNC_PROTO = CFUNCTYPE(None)

def simple_func(*args):
    print "simple_func()"
    print "args =", args

simple_func_c = SIMPLE_FUNC_PROTO(simple_func)

def pass_simple_func(func, *args):
    print "pass_simple_func()"
    print "args =", args
    func(*args)

pass_simple_func_c = SIMPLE_FUNC_PROTO(pass_simple_func)

SIMPLE_FUNC_RET_PROTO = CFUNCTYPE(c_int)

def simple_func_ret(*args):
    print "simple_func_ret()"
    print "args =", args
    return 0

simple_func_ret_c = SIMPLE_FUNC_RET_PROTO(simple_func_ret)

def pass_simple
