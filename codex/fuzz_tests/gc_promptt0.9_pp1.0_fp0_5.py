import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() frequency
#
def f():
    # just a function to stop collectable objects being deleted
    print("starting")
    yield 5
    print("ending")

def report(msg, final=False):
    print("\n%s: collectable=%s"%(msg, gc.collect(2)))

def test():
    g = f()
    r = weakref.ref(g)   # create a reference cycle
    next(g)
    report("before")

    del next(g)

    report("after 1st del")

    del g
    report("after 2nd del")


test()
