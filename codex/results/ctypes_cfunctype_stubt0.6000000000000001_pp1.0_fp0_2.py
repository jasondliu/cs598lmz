import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return "hello world"

g = fun()
print(g)

# 测试结果：
# hello world
# hello world
# 可以看出，函数中的print()能正常输出，但是返回值出错，报TypeError错误，
# 这是因为python默认返回值是None，而C语言默认返回值为0，因此会出现这样的错误。

# 解决方法
# 在函数声明的时候，指定返回值类型为ctypes.c_int即
