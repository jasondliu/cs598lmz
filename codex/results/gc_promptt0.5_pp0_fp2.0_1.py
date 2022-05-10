import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    wr = weakref.ref(a)
    gc.collect()
    if wr() is None:
        print("a was collected")
    else:
        print("a was not collected")
f()
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is None:
        print("a was collected")
    else:
        print("a was not collected")
f()
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is None:
        print("a was collected")
    else:
        print("a was not collected")
f()
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    wr =
