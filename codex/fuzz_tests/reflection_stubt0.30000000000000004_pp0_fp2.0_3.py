fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__closure__ = ()
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__globals__ = globals()
fn.__doc__ = None
fn.__text_signature__ = None
fn.__qualname__ = '<lambda>'
fn.__self__ = None
fn.__func__ = fn
fn.__class__ = <class 'function'>
fn.__call__ = <method-wrapper '__call__' of function object at 0x7f7f1c4e4b90>
fn.__get__ = <method-wrapper '__get__' of function object at 0x7f7f1c4e4b90>
fn.__set__ = <method-wrapper '__set__' of function object at 0x7f7f1c4e4b90>
fn.__del__ =
