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

# 如果没有弱引用，那么字典中的值将永远不会被回收，因为它们都有一个强引用。
# 弱引用允许对象在不再需要时被回收，因此可以使用它来解决循环引用的问题。
