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

# 弱引用字典的一个主要用途是在缓存对象的时候，可以避免缓存项目无限增长。
# 下面是一个简单的类，它可以缓存结果值，并且可以定期清除那些已经没
