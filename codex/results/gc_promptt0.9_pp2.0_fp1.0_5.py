import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
# Test gc.callbacks
class A(object):
    def __del__(self):
        pass
class B(A):
    def __del__(self):
        pass
class C(A):
    def __del__(self):
        pass
class D(C):
    pass
# Invoke gc.garbage
def foo():
    x = A()
    x = C()
    x = B()
    gc.collect()
    # But now nothing left
    gc.collect()
    # Now there are only garbage left
    cnt = [0]
    def bar(ref):
        cnt[0] += 1
    ref = weakref.ref(D())
    ref.addCallback(bar, ref)
    cnt[0] = 0
    gc.garbage.append(A())
    gc.garbage.append(D())
    gc.collect()
    assert cnt[0] == 1
    gc.garbage = gc.garbage[:1]
    gc
