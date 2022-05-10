import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

def callback(r):
    print("callback called with", r)

def test_ref():
    # Test weakref.ref()
    c = C()
    r = weakref.ref(c, callback)
    print(r)
    print(r())
    print(r is callback.__self__)
    print(r() is callback.__self__())
    c = None
    gc.collect()

def test_proxy():
    # Test weakref.proxy()
    c = C()
    p = weakref.proxy(c, callback)
    print(p)
    print(p.foo)
    print(p is callback.__self__())
    c = None
    gc.collect()

test_ref()
test_proxy()
