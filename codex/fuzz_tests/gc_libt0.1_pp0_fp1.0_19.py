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

# 弱引用字典的一个主要用途是实现缓存，比如，你可以使用它来实现一个缓存
# 对象，但是当对象不再被使用时，它会自动从缓存中清除出去。

# 弱引用字典的一个
