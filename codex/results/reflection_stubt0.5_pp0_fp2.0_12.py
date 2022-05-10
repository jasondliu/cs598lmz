fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test_fn'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None

# test_function_attributes

def test_function_attributes():
    fn = lambda: None
    assert fn.__name__ == '<lambda>'
    assert fn.__doc__ is None
    assert fn.__dict__ == {}
    assert fn.__code__.co_name == '<lambda>'
    assert fn.__code__.co_filename == '<stdin>'
    assert fn.__code__.co_flags & inspect.CO_VARARGS == 0
    assert fn.__code__.co_flags & inspect.CO_VARKEYWORDS == 0
    assert fn.__code__.co_flags & inspect.CO_NESTED == 0
    assert fn.__code__.co_flags & inspect.CO_
