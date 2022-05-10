import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello, world"
fun()

# 如果把上面的例子改成这样
@FUNTYPE
def fun():
    return 1
fun()
# 报错，因为ctypes不知道怎么处理返回值1


# 因此，指定并且调用一个函数，需要解决两个问题：
# 1. 指定一个函数的返回值
# 2. 指定一个函数可以被调用时的参数

# 将指定的函数的返回值
# ctypes.CFUNCTYPE的实例接受
