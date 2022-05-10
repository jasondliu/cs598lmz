import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 如果你只是想知道对象的内存地址，可以使用 id() 函数来获取。比如：
a = []
b = a
print(id(a))
print(id(b))

# 但是这个函数的结果并不是一个整数，而是一个长整数。
# 如果你真的需要一个整数结果，那么你可以使用 Python 的内置的 hash() 函数，比如：
print(hash(a))

# 另外，如果你
