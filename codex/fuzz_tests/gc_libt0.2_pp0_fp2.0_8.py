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

# 如果你想要构建一个能够控制对象生命周期的缓存，可以使用一个 WeakValueDictionary。
# 这个类的行为就像是一个常规的字典，但是它只会保留对象引用直到它们被垃圾回收为止。
#
