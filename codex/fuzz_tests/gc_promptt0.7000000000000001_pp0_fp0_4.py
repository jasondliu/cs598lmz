import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
def f1(p1, p2):
    a = p1
    b = p2
    del p1, p2
    class C(object):
        def __del__(self):
            print(a, b)
    return C()

def f2(p1, p2):
    a = p1
    b = p2
    del p1, p2
    class C(object):
        def __del__(self):
            print(a, b)
    return C()

def f3(p1, p2):
    a = p1
    b = p2
    del p1, p2
    return lambda: print(a, b)

def f4(p1, p2):
    a = p1
    b = p2
    del p1, p2
    return lambda: print(a, b)

def f5(p1, p2):
    a = p1
    b = p2
    del p1, p2
    return lambda: print(a,
