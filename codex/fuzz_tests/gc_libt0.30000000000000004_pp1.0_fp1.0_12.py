import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
gc.collect()

d['primary']

# 使用弱引用的字典，可以在对象不再需要的时候自动清理它们。
# 这种方式通常用于实现缓存。
# 如果你有一个对象实例，并且希望在它不再被使用的时候将其从缓存中清除
