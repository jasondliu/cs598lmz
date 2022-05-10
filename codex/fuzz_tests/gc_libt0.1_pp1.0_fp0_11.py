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

# 可以看到，在del a之后，d['primary']仍然可以访问到a的值，但是如果再次执行gc.collect()，则会报错
# 因为a已经被回收了

# 另外，如果我们把d['
