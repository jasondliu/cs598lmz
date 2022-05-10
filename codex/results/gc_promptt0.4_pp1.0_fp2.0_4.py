import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Test the collection of a cyclic list with a finalizer.

class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

def finalize(a):
    global finalize_called
    finalize_called = 1

# Finalize a
w = weakref.ref(a, finalize)

gc.collect()
assert finalize_called == 1

# Finalize b
w = weakref.ref(b, finalize)

finalize_called = 0
gc.collect()
assert finalize_called == 1

# Test the collection of a cyclic list with a finalizer.

a = A()
b = B()
a.b = b
b.a = a

def finalize(a):
    global finalize_called
    finalize_called = 1

# Finalize a
w = weakref.ref(a, finalize)

gc.collect()
assert finalize_called == 1

# Finalize b
w
