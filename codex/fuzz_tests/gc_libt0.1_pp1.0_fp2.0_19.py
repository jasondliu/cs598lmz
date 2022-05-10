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

# 如果没有弱引用，那么对象a的引用计数永远不会为0，因为字典d中有一个引用。
# 如果使用弱引用，那么当对象a被删除后，它的引用计数会变为0，并且会被
