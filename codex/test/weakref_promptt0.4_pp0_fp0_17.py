import weakref
# Test weakref.ref
import gc
import sys

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
gc.collect()

print(r())

class MyList(list):
    pass

l = MyList(range(10))
r = weakref.ref(l)

print(r)
print(r())

del l
gc.collect()

print(r())

class C:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return 'C({!r})'.format(self.a)

obj = C(10)
r = weakref.ref(obj)
print(r)
print(r())

del obj
gc.collect()

print(r())

# Test weakref.WeakKeyDictionary

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d['foo'] = o
