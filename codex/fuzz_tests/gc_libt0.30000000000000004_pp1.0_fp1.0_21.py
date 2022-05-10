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

# WeakValueDictionary
# 一个弱引用的字典，弱引用的字典的值是弱引用的，当值的引用计数为0时，会自动从字典中删除
# 可以用来实现缓存，当缓存中的对象没有被引用时，会自
