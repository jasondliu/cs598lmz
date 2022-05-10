fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__module__ = '__main__'

def test_func_code():
    assert isinstance(fn.__code__, types.CodeType)
    assert fn.__code__.co_filename == '<stdin>'
    assert fn.__code__.co_name == '<lambda>'
    assert fn.__code__.co_firstlineno == 1

def test_func_code_defaults():
    assert fn.__defaults__ == ()
    assert fn.__kwdefaults__ == None

def test_func_code_annotations():
    assert fn.__annotations__ == {}

def test_func_code_closure():
    assert fn.__closure__ == None

def test_func_code_doc():
    assert fn.__doc__ == None

def test_func_code_globals():
    assert fn.__globals__ == globals()

def test_func_code_dict():
    assert fn.__dict__
