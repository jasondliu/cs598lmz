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
# 弱引用字典，字典中的值是弱引用，当引用的对象被删除时，字典中的值也会被删除
# 弱引用字典的值不会影响对象的生命周期

# weakref.WeakKeyDictionary()
# 弱引用字典
