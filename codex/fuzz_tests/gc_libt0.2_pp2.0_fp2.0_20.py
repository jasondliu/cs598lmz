import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10

# 弱引用字典中的值不会增加对象的引用计数，因此当对象的引用计数为0时，它会被垃圾回收。
# 如果你尝试访问被回收的对象，会得到一个 KeyError 异常。

# 弱引用
