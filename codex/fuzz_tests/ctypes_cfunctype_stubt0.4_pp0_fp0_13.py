import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())

# 函数指针
fun_pointer = FUNTYPE(fun2)
print(fun_pointer())

# 函数指针数组
fun_pointer_array = (FUNTYPE * 2)(fun, fun2)
print(fun_pointer_array[0]())
print(fun_pointer_array[1]())

# 函数指针数组指针
fun_pointer_array_pointer = (FUNTYPE * 2)(fun, fun2)
print(fun_pointer_array_pointer[0]())
print(fun_pointer_array_pointer[1]())
