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

# 如果没有弱引用，那么这个字典中的值将永远不会被回收。
# 但是，如果使用了弱引用，那么当对象被垃圾回收时，字典中的条目就会自动被删除了。

# 弱引用
