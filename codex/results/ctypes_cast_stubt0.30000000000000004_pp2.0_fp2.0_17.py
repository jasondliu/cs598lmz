import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# 对于不可变类型来说，虽然无法修改它的值，但是可以给它重新赋值，比如整数。
a = 1
id(a)
a = 2
id(a)

# 对于可变类型来说，虽然可以修改它的值，但是无法给它重新赋值，比如列表。
a = [1, 2, 3]
id(a)
a.append(4)
id(a)
a = [4, 5, 6]
id(a)

# 对于不可变类
