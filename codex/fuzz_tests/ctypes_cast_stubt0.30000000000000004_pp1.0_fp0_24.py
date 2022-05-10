import ctypes
ctypes.cast(0, ctypes.py_object).value

# 注意：这个方法只能用于Python2.x，Python3.x中已经没有ctypes模块了。
# 总结
# 在Python中，类型属于对象，变量是没有类型的：
#
# a = [1, 2, 3]
#
# Here, a is a variable, and the type of a is list.
#
# 可以通过内置函数type()查询变量所指的对象类型。
#
# 如果一个变量a指向一个对象，那么，可以
