import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def f():
    a = Foo()
    b = Foo()
    a.b = b
    b.a = a
    del a, b

for i in range(10):
    f()
    gc.collect()

# Test weakref.WeakKeyDictionary.

class Foo(object):
    pass

d = weakref.WeakKeyDictionary()

def f():
    a = Foo()
    b = Foo()
    d[a] = b
    d[b] = a
    del a, b

for i in range(10):
    f()
    gc.collect()

# Test weakref.WeakValueDictionary.

class Foo(object):
    pass

d = weakref.WeakValueDictionary()

def f():
    a = Foo()
    b = Foo()
    d[a] = b
    d[b] = a
    del a, b

for i in range(10):
    f()
    gc.collect()
