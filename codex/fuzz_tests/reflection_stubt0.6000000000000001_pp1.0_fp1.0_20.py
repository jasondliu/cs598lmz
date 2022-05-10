fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = globals()
fn.__name__ = 'test'

def test():
    with pytest.raises(TypeError):
        yield 1

def test_call_it():
    test()

def test_get_code():
    assert fn.__code__.co_varnames == ('i',)

def test_get_code_default():
    assert fn.__code__.co_name == '&lt;lambda&gt;'

def test_get_defaults():
    assert fn.__code__.co_consts == (None,)

def test_get_kwdefaults():
    assert fn.__code__.co_kwonlyargcount == 0

def test_get_names():
    assert fn.__code__.co_names == ('pytest', 'test', 'raises', 'TypeError')

def test_get_stacksize():
    assert fn.__code__.co_stacksize == 2

def test_get_filename():
    assert fn
