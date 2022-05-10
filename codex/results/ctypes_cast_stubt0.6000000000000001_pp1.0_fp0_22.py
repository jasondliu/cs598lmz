import ctypes
ctypes.cast(id(v), ctypes.py_object).value

# 对于对象的引用计数
sys.getrefcount(v)

# 引用计数的改变
a = [1, 2, 3]
b = a
sys.getrefcount(a)
# 3
del b
sys.getrefcount(a)
# 2


# 容器对象的引用计数
a = [1, 2, 3]
b = a
sys.getrefcount(a)
# 3
b.append(4)
sys.getrefcount(a)
# 3

# 对象的id
id(a)
# 140566400685760

# 容器的引用计数的改变
a = [1, 2, 3]
b = a
sys.getrefcount(a)
# 3
b = a[
