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

# 弱引用字典中的值是弱引用，所以当引用的对象被删除时，这个值会被自动删除。
# 弱引用字典的一个主要用途是作为缓存，比如，你可以使用它来缓存网络或磁
