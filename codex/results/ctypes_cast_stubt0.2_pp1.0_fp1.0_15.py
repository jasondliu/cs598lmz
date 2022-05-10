import ctypes
ctypes.cast(0, ctypes.py_object).value

# 如果你想构造一个数组，并且想直接把它填充为一个特定的值，那么使用构造器函数会比较快。
# 比如，下面这个例子创建一个值都为 1 的数组：
numpy.ones(10)

# 如果你想要创建一个计数数组，可以使用 arange 函数。
# 它接受一个起始值，一个终止值和一
