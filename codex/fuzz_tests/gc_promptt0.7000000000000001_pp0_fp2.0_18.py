import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class C:
    pass

def foo():
    a = C()
    b = C()
    wr = weakref.ref(a)
    b.next = a
    a.next = b
    del a
    del b
    gc.collect()
    assert wr() is None

# Check the combination of __del__ and weakrefs

def get_A():
    class A:
        def __del__(self):
            try:
                x = self.wr()
            except ReferenceError:
                pass
            else:
                x.next = None
    a = A()
    a.wr = weakref.ref(a)
    return a

def test_del_with_weakref():
    a = get_A()
    b = get_A()
    a.next = b
    b.next = a
    del a
    del b
    gc.collect()
    gc.collect()
    gc.collect()

def test_del_with_weakref_cycle():
    import
