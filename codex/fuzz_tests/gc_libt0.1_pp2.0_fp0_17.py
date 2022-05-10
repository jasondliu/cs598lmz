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
# 当你构建一个缓存的时候，你需要考虑清除旧的缓存项。 一个简单的方式是使用一个普通的
