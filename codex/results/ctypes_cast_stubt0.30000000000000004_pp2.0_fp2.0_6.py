import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 在Python中，一个对象的引用计数增加的三种方式：
# 1. 对象被创建时，引用计数为1
# 2. 对象被引用时，引用计数加1
# 3. 对象作为参数传递给函数时，引用计数加1
# 引用计数减少的情况：
# 1. 对象别名被显式销毁 del
# 2. 对象别名被赋予新的对象
#
