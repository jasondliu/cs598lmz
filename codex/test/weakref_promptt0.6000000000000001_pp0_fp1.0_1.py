import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):

    def __init__(self):
        self.x = 1

def foo_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r().x == 1
    assert r().__class__ is Foo
    f.x = 2
    assert r().x == 2
    del f
    raises(ReferenceError, lambda: r().x)

def foo_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p.x == 1
    assert p.__class__ is Foo
    f.x = 2
    assert p.x == 2
    del f
    raises(ReferenceError, lambda: p.x)

def foo_proxy_callable():
    class C(object):
        def __init__(self):
            self.x = 1
        def foo(self):
            return self.x
    f = C()
    p = weakref.proxy(f)
    assert p.foo() == 1
    f.x
