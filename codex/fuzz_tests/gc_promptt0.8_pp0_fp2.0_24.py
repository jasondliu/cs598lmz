import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Note: empty cleanup tries to destroy gc, which produces a crash
def cleanup():
    pass
w = weakref.ref(cleanup)
del cleanup
gc.collect()
del w
gc.collect()

# test weakref.proxy()
def f():
    d = weakref.proxy(D())
    try:
        d.x = 1
        raise TestFailed, "can set attribute of weakly referencable instance"
    except TypeError:
        pass
    return d

def g():
    try:
        weakref.proxy(int)
        raise TestFailed, "can create weak reference to type"
    except TypeError:
        pass

def h():
    i = iter([1,2,3])
    try:
        weakref.proxy(i)
        raise TestFailed, "can create weak reference to iterator"
    except TypeError:
        pass

def i():
    try:
        weakref.proxy(str)
        raise TestFailed, "can create weak reference to str"
    except TypeError:
       
