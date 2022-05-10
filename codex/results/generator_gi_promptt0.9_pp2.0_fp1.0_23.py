gi = (i for i in ())
# Test gi.gi_code == None for generators without __code__
assert repr(gi.gi_frame.f_lasti) == "<unknown>"
# Test f_lasti and f_lineno propagation on block stacks
def test_gi_f_lasti():
    def foo():
        if True:
            def bar():
                return 2
            x = bar()
        else:
            def bar():
                return 3
            x = bar()
        return x
    assert foo() == 2
# test that class methods have qualified names
def test_classmethod_name():
    class A:
        @classmethod
        def foo(cls): pass
    assert A.foo.__name__ == "foo"
    assert A.foo.__qualname__ == "A.foo"
    def deco(a):
        def inner(func):
            return func
        return inner
    class A:
        @property
        @deco("hello")
        @classmethod
        def foo(cls):
            pass
    assert A.foo.__name__ == "foo"
    assert A.foo.__
