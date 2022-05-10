import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect (and indirectly gc.callbacks) with weakrefs

# register some callbacks with different priorities
class A:
    pass

class B(A):
    pass

class C(A):
    pass

callback_results = []
def callback(ignored):
    callback_results.append(1)

wr_callback_results = []
def wr_callback(wr, ignored):
    wr_callback_results.append(1)

class D:
    pass

# Create some objects, add some garbage
a = A()
b = B()
c = C()
d = D()

wr_a = weakref.ref(a)
wr_b = weakref.ref(b)
wr_c = weakref.ref(c)
wr_d = weakref.ref(d)

callback_a = gc.callbacks.create_weakref(callback, a)
callback_b = gc.callbacks.create_weakref(callback, b)
callback_c = gc.callbacks.create_weakref(callback, c)
callback
