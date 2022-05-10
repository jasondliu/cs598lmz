import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes调用C语言的动态库

# 在Python中调用C语言的动态库，需要用到ctypes模块。
#
# ctypes的使用方法是，先把C语言的动态库载入，然后，逐个函数指定函数原型。
#
# 例如，我们要调用一个名为libc.so的C动态库，里面定义了一个函数int add(int, int)。
#
# 用Python代码调用这个函数
