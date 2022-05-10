import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 用约定的方式把自定义对象变成可散列的
import collections
class MyObj(object):
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
a = MyObj(5)
b = MyObj(5)
print(hash(a), hash(b))

# collections.Hashable
isinstance(a, collections.Hashable)

# 通过让一个元组或者其他不可变的容器对象来表示
a = 1, 2, 3
b = (1, 2, 3)
print(hash(a), hash(b))

# 可变集合对象不能作为字典的键
#
