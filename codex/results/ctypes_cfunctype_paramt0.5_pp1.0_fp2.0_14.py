import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_function(a, b):
    print("my_function called with %d and %d" % (a, b))
    return a + b
f = FUNTYPE(my_function)
print(f(1, 2))

# 在Python中，我们可以使用ctypes模块来调用C库，但是需要自己编译一个C函数库。
#
# 编译后的C函数库可以在Python中被调用，这样就可以在Python中调用C函数了。
#
# 我们可以使用ctypes模块来调用C函数库，
