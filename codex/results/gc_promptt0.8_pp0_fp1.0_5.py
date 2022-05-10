import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect to ensure that it is not confused by the special GC flags
# that are set by the weakref module.  The flags should be cleared automatically
# as weakref objects are collected.

class A(object):
    pass
a = A()
wr = weakref.ref(a)
A()    # Make sure a does not get collected
del a
gc.collect()

a = A()
wr = weakref.ref(a)
del a
gc.collect()

a = A()
wr = weakref.ref(a)
del a
gc.collect()

a = A()
wr = weakref.ref(a)
del a
gc.collect()

a = A()
wr = weakref.ref(a)
del a
gc.collect()

a = A()
wr = weakref.ref(a)
del a
gc.collect()

# Test correct detection of __del__ being defined

class Foo(object):
    def __del__(self):
        pass

print weakref.ref(Foo())() is None

class Bar(object
