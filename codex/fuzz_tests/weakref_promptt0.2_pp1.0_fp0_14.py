import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

def callback(r):
    print("callback called with", r)

def test_ref():
    f = Foo()
    r = weakref.ref(f, callback)
    print(r)
    print(r())
    print(r() is f)
    print(r() is None)
    del f
    print(r() is None)

def test_proxy():
    f = Foo()
    p = weakref.proxy(f, callback)
    print(p)
    print(p.__class__)
    print(p.__dict__)
    print(p.__weakref__)
    print(p is f)
    print(p.__dict__ is f.__dict__)
    print(p.__weakref__ is f.__weakref__)
    del f
    try:
        print(p.__dict__)
    except ReferenceError:
        print("ReferenceError")

test_ref()
test_proxy()
