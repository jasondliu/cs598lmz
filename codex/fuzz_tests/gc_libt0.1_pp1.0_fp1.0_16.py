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

# 弱引用字典的一个主要用途是实现缓存。例如，你可以使用它来实现一个缓存对象，
# 并只在缓存中保留最多 N 个对象。下面是一个简单的实现：

import weakref

class Cache:
    def __init__(self, size
