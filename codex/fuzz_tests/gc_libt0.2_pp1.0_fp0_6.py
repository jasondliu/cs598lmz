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

# 弱引用的字典，当引用的对象被删除时，字典中的键值对也会被删除。
# 弱引用的字典可以用来缓存对象，但是不用担心缓存的对象无法被垃圾回收。
# 弱引用的
