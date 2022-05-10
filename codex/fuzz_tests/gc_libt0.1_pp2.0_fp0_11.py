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
for key, value in d.items():
    print key, value
del a
print 'after del a'
gc.collect()
for key, value in d.items():
    print key, value

print '\n'

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
for key, value in d.items():
    print key, value
del a
print 'after del a'
for key, value in d.items():
    print key, value

print '\n'

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
for key, value in d.items
