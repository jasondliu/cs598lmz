import gc, weakref, sys

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

# 可以看到，在删除a之后，d['primary']的值也被删除了
# 可以用这个特性来实现缓存，比如缓存网页
# 如果缓存的数据量大，可以用weakref.WeakKeyDictionary()来实现
# 如果缓存的数
