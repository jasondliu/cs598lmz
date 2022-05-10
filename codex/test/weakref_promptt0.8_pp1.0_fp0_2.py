import weakref
# Test weakref.ref(lambda: 0)
def test_function_ref():
    f = lambda: 0
    wr = weakref.ref(f)
    assert wr() is f
    del f
    assert wr() is None
    # create a method by binding a function to an instance
    class Foo:
        func = lambda: 0
    foo = Foo()
    fooref = weakref.ref(foo.func)
    assert fooref() is foo.func
    del foo
    assert fooref() is None
    # create a function by applying a decorator to a function
    def deco(f):
        def inner():
            return 0
        return inner
    g = deco(lambda: 0)
    assert g() == 0
    assert not hasattr(g, '__func__')
    gref = weakref.ref(g)
    assert gref() is g
    del g
    assert gref() is None

# temporary workaround to avoid creating a cycle
# Python/ceval.c::PyEval_EvalCodeEx() doesn't check recursion
# depth when
