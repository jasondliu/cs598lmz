import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after the weakref callback has been invoked.

class A:
    pass

def foo(w):
    print('foo called')

a = A()

# Without this line, the test fails.  I don't know why.
print(bin(id(a)))

wr = weakref.ref(a, foo)

del a

gc.collect()
print('end of test')
