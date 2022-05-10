import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
import os, sys
print('nt:', sys.getrefcount(None))
p = weakref.proxy(None)
print('nt:', sys.getrefcount(None))
del p
print('nt:', sys.getrefcount(None))
gc.collect()
print('nt:', sys.getrefcount(None))
class C:
    pass
c = C()
def foo():
    return c
print('c  :', sys.getrefcount(c))
print('foo:', sys.getrefcount(foo))
p = weakref.proxy(foo)
print('c  :', sys.getrefcount(c))
print('foo:', sys.getrefcount(foo))
print('p  :', sys.getrefcount(p))
print('p():', p())
del foo, c
print('p():', p())
gc.collect()
print('p():', p())
class C:
    pass
c = C()
print('c:', sys.getrefcount(c))
p = weakref.proxy(c)
print
