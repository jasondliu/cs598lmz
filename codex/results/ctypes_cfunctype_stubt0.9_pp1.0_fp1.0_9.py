import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "This works fine"
    return 42
from python_cffi_call_a_c_function import *
fun2 = get_fun()
result = fun2()
print result
