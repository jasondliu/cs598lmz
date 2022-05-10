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
print d.items()
del a
print 'after del a'
print d.items()

print 'before gc.collect()'
print d.items()
gc.collect()
print 'after gc.collect()'
print d.items()

print 'before a = A(20)'
print d.items()
a = A(20)
print 'after a = A(20)'
print d.items()

print 'before d["primary"] = a'
print d.items()
d['primary'] = a
print 'after d["primary"] = a'
print d.items()

print 'before del a'
print d.items()
del a
print 'after del a'
print d.items()

print 'before g
