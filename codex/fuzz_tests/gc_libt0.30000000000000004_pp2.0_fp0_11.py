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

# 弱引用的字典是一个类似字典的容器，它只保存对象的弱引用而不是强引用。
# 弱引用的字典的主要用途是作为缓存，它的键可以是任何的不可变类型，而值是对象的弱引用。
#
