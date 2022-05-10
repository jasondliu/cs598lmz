import weakref
# Test weakref.ref leaks.

import gc
import copy

class A(object):
    pass

a = A()

def fn():
    r = weakref.ref(a)
    del r
    r = weakref.ref(a)
    del r

for i in range(100):
    fn()
    gc.collect()
