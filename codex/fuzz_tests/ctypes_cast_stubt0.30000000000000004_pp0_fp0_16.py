import ctypes
ctypes.cast(1, ctypes.py_object)

# 在Python中，类型属于对象，变量是没有类型的
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
# 变量只是用来指向一个对象的指针，对象包含实际的数据。

a = [1, 2, 3]
b = a
a.append(4)
b
# [1, 2, 3, 4]

# 数字类型
# Python3 支持 int、float、bool、complex（复数
