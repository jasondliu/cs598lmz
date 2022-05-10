from ctypes import *
FUNTYPE = CFUNCTYPE(c_char_p)
@FUNTYPE
def fun():
    return 'hello'
fun(1,2)
