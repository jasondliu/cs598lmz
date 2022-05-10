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

# 弱引用的字典可以被用来缓存对象，并且只要对象还被其他地方引用，它就可以被安全的使用。
# 如果对象被垃圾回收机制回收，那么相应的字典条目会被删除。
# 弱
