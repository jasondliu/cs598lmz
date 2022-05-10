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

# 如果没有弱引用，那么字典中的值将会一直存在，即使它的原始对象已经被删除了。
# 弱引用允许垃圾回收机制回收对象，而不用担心引用对象还存在。
# 弱引
