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

# 弱引用字典的主要用途是在缓存对象的时候，它可以在缓存对象的同时，不增加对象的引用计数。
# 弱引用字典的一个限制是它的键必须是不可变的。
# 弱引用字典的另一个
