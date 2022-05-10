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

# 弱引用字典的一个主要用途是实现缓存。
# 例如，如果你有一个计算成本很高的函数，并且需要缓存结果，那么可以使用一个弱引用字典来缓存结果。
# 下面是一
