import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()将一个整数转换成一个指针，然后通过.value属性访问指针指向的内存区域。
# 如果你想要的是一个指针的整数值，可以使用ctypes.addressof()函数。

# 在ctypes中，指针的行为和普通的Python整数类型很相似。
# 例如，指针支持标准的数学运算，比如加法和减法。

