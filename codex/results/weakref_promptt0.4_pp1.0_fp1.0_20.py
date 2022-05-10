import weakref
# Test weakref.ref(obj)

def test_weakref_ref():
    class Foo(object):
        pass
    foo = Foo()
    foo.bar = Foo()
    foo.bar.foo = foo
    foo.bar.l = [foo]
    foo.bar.d = {'foo': foo}
    foo.bar.s = set([foo])
    foo.bar.f = lambda: foo
    foo.bar.c = weakref.ref(foo)
    foo.bar.m = weakref.ref(foo.bar)
    r = weakref.ref(foo)
    assert r() is foo
    assert r().bar is foo.bar
    assert r().bar.foo is foo
    assert r().bar.l[0] is foo
    assert r().bar.d['foo'] is foo
    assert r().bar.s.pop() is foo
    assert r().bar.f() is foo
    assert r().bar.c() is foo
    assert r().bar.m() is foo.bar
    del foo
    raises(ReferenceError, "r()")
   
