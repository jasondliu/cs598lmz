import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() right away.  This should really collect something.
gc.collect()

class A:
    def __init__(self, value=1):
        self.value = value
    def __repr__(self):
        return '<A %r>' % self.value

a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
d['alias'] = a
del a           # remove the one reference to a
assert not gc.collect()     # a is still alive because it's in the dict
del d['primary']
assert gc.collect()         # a should die now

a1 = A(1)
print(a1)
d1 = weakref.WeakValueDictionary()
d1['1'] = a1
print(d1.data)
print(d1.data.popitem())
print(d1.data)
print('-'*20)
print(d1)
del a1
print(d1)
print('-'*20)
gc.collect()
print(d1)
print('-'*
