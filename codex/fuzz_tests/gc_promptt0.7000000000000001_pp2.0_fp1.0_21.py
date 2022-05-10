import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref. This object should be collected.
# This test currently fails.

class A:
    pass

def my_del(w, id):
    print('my_del called with %s' % (w,))

a = A()
b = A()
a.b = b
b.a = a
a.count = b.count = 1

a_wr = weakref.ref(a, my_del)
b_wr = weakref.ref(b, my_del)

del a
del b

gc.collect()
print(gc.collect())
print(a_wr(), b_wr())

# Test gc.collect() with a weakref. This object should not be collected.
# This test passes.

class B:
    pass

def my_del(w, id):
    print('my_del called with %s' % (w,))

a = B()
a.b = 4
a_wr = weakref.ref(a, my_del)

del a

gc.collect()
print
