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

# 可以看到，在删除对象a之后，d['primary']仍然可以访问到对象a的值，
# 这是因为weakref.WeakValueDictionary()中的值是弱引用，
# 当对象a被删除后，d['primary']中的值也
