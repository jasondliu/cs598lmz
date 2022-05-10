import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() vs. gc.collect(1).  The former collects
# all unreachable objects, while the latter only collects
# unreachable objects that are containers.
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(object):
    pass

class F(object):
    pass

def check_garbage(obj, name, container, collectable):
    gc.collect()
    gc.collect(1)
    if container:
        assert not gc.is_tracked(obj), name
    else:
        assert gc.is_tracked(obj), name
    if collectable:
        assert gc.is_tracked(obj), name
        assert not gc.is_marked(obj), name
    else:
        assert not gc.is_tracked(obj), name

def check_ok(obj, name, container, collectable):
    check_garbage(obj, name, container, collectable)
    del obj

