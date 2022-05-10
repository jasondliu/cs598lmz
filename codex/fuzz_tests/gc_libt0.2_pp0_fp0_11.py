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

# 弱引用的字典，当引用的对象被删除后，字典中的值也会被删除

# 弱引用的字典，当引用的对象被删除后，字典中的值也会被删除

# 弱引用的字典，当引用的对
