fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.__code__

def test_func_code():
    def f(): pass
    assert f.__code__.co_varnames == ('f',)
    assert f.__code__.co_argcount == 0
    assert f.__code__.co_consts == ()
    assert f.__code__.co_filename == __file__
    assert f.__code__.co_name == 'f'
    assert f.__code__.co_firstlineno == 5
    assert f.__code__.co_flags == 67
    assert f.__code__.co_stacksize == 1

    def f(x): pass
    assert f.__code__.co_varnames == ('x', 'f')
    assert f.__code__.co_argcount == 1
    assert f.__code__.co_consts == ()
    assert f.__code__.co_filename == __file__
    assert f.__code__.co_name == 'f'
    assert f.__code__.
