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

# 如果没有弱引用，那么字典中的值将会是一个无效的引用，因为对象已经被删除了。
# 弱引用的一个主要用途是实现缓存。比如，如果你想实现一个缓存，但是不希望
