import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with cyclic garbage and weakrefs
# The cyclic garbage is created by a function that returns
# a list that contains a reference to itself.

def f():
    L = [None]
    L[0] = L
    return L

class A:
    pass

def callback(w):
    print 'callback', w

def test_callback():
    a = A()
    a.callback = callback
    a.callback(a)
    del a
    print 'collecting'
    gc.collect()
    print 'done'

def test_selfref():
    l = f()
    del l
    print 'collecting'
    gc.collect()
    print 'done'

def test_weakref():
    l = f()
    r = weakref.ref(l, callback)
    print 'callback should be called'
    del l
    print 'collecting'
    gc.collect()
    print 'done'

def test_weaklist():
    l = f()
    r = weakref.ref(l, callback
