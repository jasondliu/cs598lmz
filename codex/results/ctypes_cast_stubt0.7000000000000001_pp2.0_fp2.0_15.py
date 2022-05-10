import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# 可以使用实例本身作为计数器
class CountedObject:
    def __init__(self):
        self.count = 0

    def __del__(self):
        print('count =', self.count)

obj = CountedObject()
obj.count += 1
del obj

# 引用计数工作得很好，但是它有时候会出问题。例如，如果你创建了一个循环，那么这些对象就永远不会被垃圾回收了
a = [CountedObject()]
b = [a, a]


# __del__ 方法不能正
