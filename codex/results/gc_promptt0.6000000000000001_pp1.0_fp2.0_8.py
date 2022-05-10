import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
import weakref

class MyClass:
    pass

class MyClassRef(weakref.ref):
    pass

def check(a, b, c):
    print 'collecting...'
    gc.collect()
    print 'done.'
    print 'a:',
    if a() is None: print 'dead'
    else: print a(), a().__class__
    print 'b:',
    if b() is None: print 'dead'
    else: print b(), b().__class__
    print 'c:',
    if c() is None: print 'dead'
    else: print c(), c().__class__

a = MyClass()
b = MyClass()

a.attr = a
b.attr = b

check(weakref.ref(a), weakref.ref(b), weakref.ref(a))

a = MyClass()
b = MyClass()
a.attr = a
b.attr = b
a.b = b
b.a = a

check(weakref.ref
