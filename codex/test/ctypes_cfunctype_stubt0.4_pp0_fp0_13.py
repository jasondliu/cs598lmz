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
