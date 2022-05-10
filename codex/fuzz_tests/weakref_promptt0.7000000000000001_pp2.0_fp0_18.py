import weakref
# Test weakref.ref in isolation
class Tester(object):
    pass

def f(x):
    pass

def weakref_test():
    t = Tester()
    ref = weakref.ref(t, f)
    t.a = 1
    t.b = 2
    t.c = 3
    print ref() is t
    del t
    return ref

import gc
gc.collect()

ref = weakref_test()
print ref()
print ref() is None
gc.collect()
print ref()

# Test weakrefs with a non-empty __slots__
class Tester(object):
    __slots__ = ['a', 'b', 'c']

def weakref_test():
    t = Tester()
    ref = weakref.ref(t, f)
    t.a = 1
    t.b = 2
    t.c = 3
    print ref() is t
    del t
    return ref

import gc
gc.collect()

ref = weakref_test()
print ref()
print ref() is
