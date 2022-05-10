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
# 弱引用的字典，当字典中的值被删除时，字典中的键值对也会被删除
# 弱引用的字典，当字典中的值被删除时，字典中的键值对也会被删除
# 弱引用的
