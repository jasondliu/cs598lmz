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

# 弱引用字典的一个主要用途是在缓存对象的时候，可以避免缓存项目无限增长。
# 下面是一个简单的类，它利用弱引用字典来缓存对象：

import weakref

class Cache:
    def __init__(self, cache_size):
