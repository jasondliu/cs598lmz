import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun_return"

fun_return = fun()
print(fun_return)
print(type(fun_return))

print("*"*10, "callable()判断是否可调用")
fun_return1 = fun
print(callable(fun_return1))
print(callable(fun_return))

print("*"*10, "dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表")
print(dir())

