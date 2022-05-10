import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello")
    return 1

#fun()


# 第二个参数是什么意思？
# 当我们调用 fun() 时，解释器会调用 fun.__call__() 来执行函数的调用动作
fun.__call__ = lambda: 2
#fun()


# 再次调用 fun() 时，解释器调用 fun.__call__()，但是这个时候 fun.__call__() 变成了一个函数，所以我们需要调用 fun.__call__()()，再次调用 fun.__call__()() 时，需要设
