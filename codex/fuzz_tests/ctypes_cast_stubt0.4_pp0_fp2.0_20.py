import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()函数将一个整数转换成一个指针，然后调用这个指针的value属性，
# 就可以拿到这个整数对应的Python对象。

# 如果你需要获取某个对象的内存地址，可以使用id()函数。
# 你可以把这个地址转换成一个整数，再使用ctypes.cast()函数把这个整数转换成一个指
