fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__closure__ = None
fn.__globals__ = globals()
fn.__doc__ = None
fn.__text_signature__ = None
fn.__get__(None, object)
fn.__self__ = None
fn.__func__ = fn
fn.__repr__()
fn.__str__()
fn.__hash__()
fn.__call__()
fn.__dir__()
fn.__set_name__(None, 'fn')
fn.__reduce__()
fn.__reduce_ex__(2)
fn.__getstate__()
fn.__setstate__({})
fn.__format__('s')
fn.__sizeof__()
fn.__instancecheck__(object)
