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

# 如果没有弱引用，那么对象a将永远不会被回收，因为字典d中有一个强引用。
# 但是，如果使用弱引用，那么当对象a被删除后，它将被回收，并且字典中的弱引
