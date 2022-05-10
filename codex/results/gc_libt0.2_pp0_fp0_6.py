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

# 弱引用字典的一个主要用途是在缓存对象的时候。
# 例如，如果你想实现一个缓存，为了防止内存泄漏，你需要手动地清理缓存。
# 为了解决这个问题，你可
