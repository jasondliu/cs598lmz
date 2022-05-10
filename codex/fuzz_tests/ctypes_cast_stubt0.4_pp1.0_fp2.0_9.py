import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 或者使用内置的 sys 模块
import sys
sys.getrefcount(obj)

# 如果要找出对象的所有引用，可以使用 gc 模块
import gc
gc.get_referrers(obj)

# 如果要知道某个变量是否是某个对象的引用，可以使用 is 和 is not 操作符
a = [1, 2, 3]
b = a
b is a

# 但是要注意，即使两个变量名指向同一个对象，对其中一个变量
