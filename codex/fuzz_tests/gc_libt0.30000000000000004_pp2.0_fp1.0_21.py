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

# weakref.WeakValueDictionary()
# 弱引用的字典，只要没有别的引用指向 key 所对应的对象，那么这个 key 就会从字典中消失。

# 弱引用的字典，只要没有别的引用指向 key 所对应的对象，那么
