fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
bpo15393 = (not hasattr(fn, '__closure__') and
            hasattr(fn, '__code__') and
            (not hasattr(fn, '__defaults__') or
             (fn.__code__.co_flags & 0x4) == 0))

if bpo15393:
    # Issue 15393: if a function has a code object with CO_NOFREE, its
    # __code__ attribute is not writable.
    def test_func_no_free():
        assert_raises(TypeError, setattr, test_func_no_free, '__code__', 0)

    test_func_no_free.__code__ = compile('pass', '', 'exec')
    test_func_no_free = types.FunctionType(
        test_func_no_free.__code__,
        globals())

# Issue #14112: PyFunction_GetClosure() doesn't check __closure__
@cpython_only
def test_func_closure():
    def f():
        pass
    assert f.__
