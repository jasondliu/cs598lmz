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

# 弱引用字典的一个主要用途是实现缓存。
# 例如，如果你想实现一个缓存，其中包含大量的昂贵对象，但是又不想阻止它们被垃圾回收，那么可以使用一个弱引用字典
