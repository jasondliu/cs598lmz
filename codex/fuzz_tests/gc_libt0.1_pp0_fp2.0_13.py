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
# 弱引用字典的一个主要用途是实现缓存。
# 弱引用字典的一个主要用途是实现缓存。
# 弱引用字典的一个主要用途是实现缓存。
# 弱引
