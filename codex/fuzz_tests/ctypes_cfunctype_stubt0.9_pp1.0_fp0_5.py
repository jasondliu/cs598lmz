import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "function"
fun_obj = function(fun)

print repr(fun_obj)
print repr(fun_obj.py_function)
print fun_obj()

fun_obj2 = fun_obj.to_function()
print repr(fun_obj.py_function)
print fun_obj2()
