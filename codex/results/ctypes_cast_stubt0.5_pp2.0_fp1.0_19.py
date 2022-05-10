import ctypes
ctypes.cast(0, ctypes.py_object).value

# 但是，如果你打算写一个能通过多种不同方式来访问数据的数据结构，那么使用 __slots__ 是一个非常好的方式。

# 小结

# 定义了 __slots__ 变量后，Python 就会为实例使用一种更加紧凑的内部表示。
# 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字
