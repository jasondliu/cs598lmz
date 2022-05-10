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

# WeakValueDictionary 中的值对象，如果没有其他的引用，将会被垃圾回收机制回收。
# 如果值对象被回收，那么 WeakValueDictionary 中的键值对将会自动删除。
# 如果值对象被回收
