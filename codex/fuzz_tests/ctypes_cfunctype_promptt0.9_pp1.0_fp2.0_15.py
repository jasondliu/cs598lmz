import ctypes
# Test ctypes.CFUNCTYPE callback
def callback_ftype_test(j,k,l):
    print("callback_ftype_test",j," ",k," ",l)

@c_function_caller(ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p))
def test_CtypeFCallback(a,b,c):
    print("test_CtypeFCallback")
    callback(a).value.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
    callback(a).value.restype = None
    callback(a).value(atoi(b),atoi(c),"hello")

@c_function_caller(ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p))
def test_CtypeFCallback(a,b,c):
    print("test_CtypeFCallback")
    callback(a).value.arg
