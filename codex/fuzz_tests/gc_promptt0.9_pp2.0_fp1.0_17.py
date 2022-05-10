import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
def test3():
    print sys.gettotalrefcount()
    refs = []
    print gc.collect()
    print sys.gettotalrefcount()
    print gc.collect()
    print sys.gettotalrefcount()
    for i in range(10):
        #a = [1,2,3]
        a = weakref.ref(object())
        b = [a]
        c = (i, b)
        refs.append(c)
    print sys.gettotalrefcount()
    del refs
    print sys.gettotalrefcount()
    print gc.collect()
    print sys.gettotalrefcount()
def test2():
    a = [1,2,3]
    del a

    print sys.gettotalrefcount()
    print gc.collect()
    print sys.gettotalrefcount()

    a = [1,2,3]
    del a
    del a
    del a
    del a

    print sys.gettotalrefcount()
    print gc.collect()
    print sys.
