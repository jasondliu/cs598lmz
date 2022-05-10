fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# PyPy's `inspect.getclosurevars` is broken, which causes
# `trio.abc.Instrument` to be broken.
# See https://bitbucket.org/pypy/pypy/issues/2900/inspectgetclosurevars-is-broken
# for details.
if not is_pypy:
    def test_instrument():
        # Ensure that Instrument works with all of the different ways
        # that a function can have a closure.
        class C:
            pass

        # No closure
        assert not list(abc.Instrument(fn))

        # Closure from nested scope
        def f():
            x = 1
            assert list(abc.Instrument(f)) == [x]

        # Closure from nonlocal
        def g():
            x = 1

            def f():
                nonlocal x
                assert list(abc.Instrument(f)) == [x]

            return f

        g()()

        # Closure from globals
        x = 1

        def f():
            assert list(abc.
