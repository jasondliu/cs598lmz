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
#     弱引用字典，只要对象不再被引用，它就会被垃圾回收机制回收，而不管字典中是否还存在该对象的键。
#     如果对象被垃圾回收，那么字典中相
