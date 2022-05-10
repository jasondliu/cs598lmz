import weakref
# Test weakref.ref
class Test(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "<Test value=%d>" % (self.value,)
def test_ref():
    import weakref
    def create_test(i):
        return Test(i)
    x = create_test(10)
    r = weakref.ref(x)
    print r(), x
    x = create_test(20)
    print r(), x
    del x
    print r()
def test_ref_fn():
    import weakref
    def create_test(i):
        return Test(i)
    def f():
        x = create_test(10)
        r = weakref.ref(x)
        print r(), x
        x = create_test(20)
        print r(), x
        del x
        print r()
    import __pypy__
    __pypy__.run_toplevel(f)
def test_compare():
    import weakref
    x =
