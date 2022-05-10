fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'fn doc'
fn.__annotations__ = {'a': 'b'}
fn.__globals__ = {'foo': 'bar'}
fn.__closure__ = (c,)
fn.__dict__ = {'a': 'b'}
fn.__kwdefaults__ = {'a': 'b'}
fn.__defaults__ = ('a', 'b')
fn.__module__ = 'fn'
fn.__qualname__ = 'fn'
fn.__text_signature__ = '(a, b)'

def fn2():
    'fn2 doc'
    pass

def fn3(a, b=None):
    'fn3 doc'
    pass

def fn4(a, b=None, *, c=None, **kw):
    'fn4 doc'
    pass

def fn5(a, b=None, *args, c=None, **kw):
    'fn5 doc'
    pass


