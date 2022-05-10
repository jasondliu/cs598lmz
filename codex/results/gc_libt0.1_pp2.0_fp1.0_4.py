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

# 如果没有弱引用，那么这个字典中的值将永远不会被回收。
# 弱引用允许这个对象被回收，并且这个字典中的相应条目会自动被删除。
# 弱引用的一个主要用途是实
