fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_function_code():
    from sys import getrefcount as grc
    from sys import _getframe as gf
    from sys import modules as sm
    from types import FunctionType

    def f():
        pass

    def g():
        pass

    assert f.__code__ is f.__code__
    assert g.__code__ is g.__code__
    assert f.__code__ is not g.__code__

    # Make sure that the __code__ attribute doesn't keep the object alive
    # (issue #24154)
    f = FunctionType(lambda: None, {}, 'f')
    g = FunctionType(lambda: None, {}, 'g')
    f.__code__ = g.__code__
    del f
    del g
    for i in range(10):
        sm.clear()
        gc.collect()
        gc.collect()
        gc.collect()
        gc.collect()
        if grc(gf().f_code) == 2:
            break
    else:
        raise
