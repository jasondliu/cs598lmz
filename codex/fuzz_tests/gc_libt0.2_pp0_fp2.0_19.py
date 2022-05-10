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

# 上面的代码中，a 变量被删除后，对象不会被垃圾回收，因为 d 字典中还有一个弱引用指向它。
# 当字典被删除后，对象才会被垃圾回收。

# 如果一个弱引用
