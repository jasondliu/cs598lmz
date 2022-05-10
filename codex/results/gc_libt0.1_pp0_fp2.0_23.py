import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d['primary']
del a
gc.collect()
print 'after del a'
print d['primary']

# before del a
# 10
# after del a
# 10

# 如果没有弱引用，那么这个字典中的值永远不会被回收，因为字典中的值还有一个强引用。
# 如果使用弱引用，那么当对象没有其他强引用的
