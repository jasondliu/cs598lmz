import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print "func(%d)" % n
    return n * 2

f = FUNTYPE(func)
print f(5)

# 使用ctypes.CFUNCTYPE()创建一个函数类型对象，并将func()函数转换为该类型。
# 这个函数类型对象可以被调用，就像一个普通函数一样。
# 在这个例子中，func()函数的返回值被自动转换为c_int类型。
# 如果func()函数返回一
