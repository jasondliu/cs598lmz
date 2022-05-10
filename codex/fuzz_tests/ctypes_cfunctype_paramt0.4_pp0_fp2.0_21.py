import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    return n * 10

f = FUNTYPE(func)
print(f(3))

# 使用python的ctypes库来调用C语言的动态链接库
# 在C语言中，编译成动态链接库，gcc -shared -o libmylib.so mylib.c
# 在python中，
# from ctypes import *
# mylib = cdll.LoadLibrary('./libmylib.so')
# mylib.add(2,3)
# 
# 在C语言中，编译成静态库，gcc -c mylib.c
# ar rcs libmylib.a mylib.o
# 在python中，
# from ctypes import *
